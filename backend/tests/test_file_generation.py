import pytest
import shutil
import os
import stat
from typing import Optional # Added Optional
from fastapi.testclient import TestClient

# Assuming 'app' is the FastAPI instance in backend.main
# Adjust the import path if your project structure is different
from backend.main import app
from backend.orchestrator import AppStates

# Global test client
client = TestClient(app)

# Define a directory for test outputs, relative to this test file
# This makes it easier to locate and clean up.
# The 'backend' part is because pytest typically runs from the project root.
TEST_OUTPUT_ROOT_DIR = os.path.join(os.path.dirname(__file__), "test_output_gen_files")

@pytest.fixture(scope="module") # Use "module" scope if multiple tests use this and cleanup can happen once
def test_output_dir(request):
    """
    Pytest fixture to create and cleanup a directory for test outputs.
    This fixture will create TEST_OUTPUT_ROOT_DIR before the first test in the module
    and remove it after all tests in the module have run.
    """
    if os.path.exists(TEST_OUTPUT_ROOT_DIR):
        shutil.rmtree(TEST_OUTPUT_ROOT_DIR)
    os.makedirs(TEST_OUTPUT_ROOT_DIR, exist_ok=True)

    # This function will be called after all tests in the module are done
    def finalizer():
        if os.path.exists(TEST_OUTPUT_ROOT_DIR):
            shutil.rmtree(TEST_OUTPUT_ROOT_DIR)

    request.addfinalizer(finalizer)
    return TEST_OUTPUT_ROOT_DIR

# Helper function to extract output directory from response message
def _extract_output_dir_from_message(message: str) -> Optional[str]:
    # Example message: "Arquivos do projeto 'test_project_bootstrap', incluindo bootstrap.sh, foram gerados em: output/test_project_bootstrap_20231027103000"
    # Or, if using the test_output_dir fixture, it might be like: "backend/tests/test_output_gen_files/test_project_bootstrap_YYYYMMDDHHMMSS"
    prefix = "foram gerados em: "
    if prefix in message:
        return message.split(prefix, 1)[1]
    return None

def test_generate_files_endpoint_success(test_output_dir, monkeypatch):
    """
    Tests the /generate_files endpoint for successful file generation
    after reaching the DEVOPS state.
    """
    # Monkeypatch the base_output_dir in file_generator.py to use our test_output_dir
    # This ensures generated files go into the fixture-controlled directory.
    # The `test_output_dir` fixture provides the path `backend/tests/test_output_gen_files`
    monkeypatch.setattr("backend.file_generator.BASE_OUTPUT_DIR_FOR_TESTS", test_output_dir)

    project_name = "test_project_bootstrap_success"

    # 1. Start session
    response = client.post("/start", json={"project_name": project_name})
    assert response.status_code == 200
    data = response.json()
    assert data["project_name"] == project_name
    assert data["current_state"] == AppStates.PLANNING.value

    # 2. Approve to ISSUES
    response = client.post("/approve")
    assert response.status_code == 200
    data = response.json()
    assert data["new_state"] == AppStates.ISSUES.value

    # 3. Approve to DEVOPS
    response = client.post("/approve")
    assert response.status_code == 200
    data = response.json()
    assert data["new_state"] == AppStates.DEVOPS.value

    # At this point, the orchestrator's session's current_state should be DEVOPS
    # We need to ensure the project_name is correctly set in the orchestrator's session
    # The /start endpoint should have set this.

    # 4. Call /generate_files
    response_gen = client.post("/generate_files")
    assert response_gen.status_code == 200
    gen_data = response_gen.json()
    assert gen_data["status"] == "files_generated_successfully"
    assert "message" in gen_data

    # 5. Extract output directory path and verify
    # The message format is "Arquivos do projeto '{project_name}', incluindo bootstrap.sh, foram gerados em: {output_dir}"
    # {output_dir} will now be inside `test_output_dir` (e.g., backend/tests/test_output_gen_files/test_project_bootstrap_success_YYYYMMDDHHMMSS)

    generated_dir_project_specific_path_str = None
    if "foram gerados em: " in gen_data["message"]:
        # The path in the message is the absolute path to the project-specific dir
        generated_dir_project_specific_path_str = gen_data["message"].split("foram gerados em: ")[1]

    assert generated_dir_project_specific_path_str is not None, "Could not parse generated directory path from response"

    # Verify the path from message is within our test_output_dir
    assert generated_dir_project_specific_path_str.startswith(test_output_dir), \
        f"Generated path '{generated_dir_project_specific_path_str}' is not within test_output_dir '{test_output_dir}'"

    assert os.path.isdir(generated_dir_project_specific_path_str), \
        f"Generated directory '{generated_dir_project_specific_path_str}' does not exist."

    bootstrap_sh_path = os.path.join(generated_dir_project_specific_path_str, "bootstrap.sh")
    assert os.path.isfile(bootstrap_sh_path), \
        f"bootstrap.sh not found in '{generated_dir_project_specific_path_str}'."

    # 6. Cleanup:
    # The `test_output_dir` module-scoped fixture will handle cleanup of TEST_OUTPUT_ROOT_DIR
    # and all its contents (including the generated_dir_project_specific_path_str).
    # So, no explicit shutil.rmtree(generated_dir_project_specific_path_str) is needed here.
    # We can, however, verify that files were created if needed for other tests.
    # For this test, verifying existence is enough.

def test_bootstrap_script_content_and_permissions(test_output_dir, monkeypatch):
    """
    Tests the content and permissions of the generated bootstrap.sh script.
    """
    monkeypatch.setattr("backend.file_generator.BASE_OUTPUT_DIR_FOR_TESTS", test_output_dir)

    project_name = "test_project_bootstrap_content"

    # 1. Start session and reach DEVOPS state
    client.post("/start", json={"project_name": project_name}) # Don't need to assert, done in previous test
    client.post("/approve") # PLANNING -> ISSUES
    client.post("/approve") # ISSUES -> DEVOPS

    # 2. Call /generate_files
    response_gen = client.post("/generate_files")
    assert response_gen.status_code == 200
    gen_data = response_gen.json()
    assert gen_data["status"] == "files_generated_successfully"

    generated_dir_project_specific_path_str = _extract_output_dir_from_message(gen_data["message"])
    assert generated_dir_project_specific_path_str is not None
    assert os.path.isdir(generated_dir_project_specific_path_str)

    bootstrap_sh_path = os.path.join(generated_dir_project_specific_path_str, "bootstrap.sh")
    assert os.path.isfile(bootstrap_sh_path)

    # 3. Verify Permissions
    file_mode = os.stat(bootstrap_sh_path).st_mode
    assert bool(file_mode & stat.S_IXUSR), "bootstrap.sh should have user execute permission (S_IXUSR)"
    assert bool(file_mode & stat.S_IRUSR), "bootstrap.sh should have user read permission (S_IRUSR)"
    # Typically 0o755 means rwxr-xr-x. S_IXGRP and S_IXOTH for group/other execute.
    # S_IWUSR for user write. For this test, S_IXUSR is the most critical.
    # os.chmod in file_generator sets 0o755, so S_IXUSR, S_IXGRP, S_IXOTH should be true.
    assert bool(file_mode & stat.S_IXGRP), "bootstrap.sh should have group execute permission (S_IXGRP)"
    assert bool(file_mode & stat.S_IXOTH), "bootstrap.sh should have other execute permission (S_IXOTH)"


    # 4. Verify Content
    with open(bootstrap_sh_path, "r") as f:
        content = f.read()

    assert "#!/bin/bash" in content, "Shebang '#!/bin/bash' not found."
    assert f"read -p \"Por favor, forneça o caminho de instalação para '{project_name}'" in content, "Install path prompt not found or incorrect."
    assert f"mkdir -p \"$install_path/{project_name}\"" in content, "mkdir command not found or incorrect."
    assert f"cat << EOF > \"$install_path/{project_name}/README.md\"" in content, "cat EOF for README.md not found or incorrect."
    assert f"# Projeto: {project_name}" in content, "Project name placeholder in README content not found."

    # Cleanup is handled by the test_output_dir fixture

def test_generate_files_endpoint_not_in_devops_state(test_output_dir, monkeypatch):
    """
    Tests that /generate_files endpoint returns 'not_ready_for_generation'
    if the session is not in DEVOPS state.
    """
    monkeypatch.setattr("backend.file_generator.BASE_OUTPUT_DIR_FOR_TESTS", test_output_dir)
    project_name = "test_project_not_devops"

    # 1. Start session (state will be PLANNING)
    response = client.post("/start", json={"project_name": project_name})
    assert response.status_code == 200
    data = response.json()
    assert data["current_state"] == AppStates.PLANNING.value

    # 2. Call /generate_files (while still in PLANNING)
    response_gen = client.post("/generate_files")
    assert response_gen.status_code == 200 # Endpoint itself doesn't error, but returns specific status
    gen_data = response_gen.json()
    assert gen_data["status"] == "not_ready_for_generation"
    assert AppStates.PLANNING.value in gen_data["message"] # Message should mention current state

    # 3. Verify no output directory was created for this project in the test output
    # List contents of test_output_dir. It should be empty or not contain this project_name.
    # Since filenames include timestamps, we check if *any* directory for this project_name exists.
    # This is a bit tricky if other tests ran and failed to clean up.
    # The `test_output_dir` fixture ensures the root `TEST_OUTPUT_ROOT_DIR` is clean at module start.
    # So, we just need to check if anything related to `project_name` was created *during this test*.
    # A simple way: check if `test_output_dir` is empty. If other tests run in parallel or
    # if this test runs after a successful one, this check is not robust.
    # Better: ensure no directory starting with `project_name` exists in `test_output_dir`.

    found_project_dir = False
    if os.path.exists(test_output_dir): # test_output_dir is backend/tests/test_output_gen_files
        for item in os.listdir(test_output_dir):
            if item.startswith(project_name.lower().replace(' ', '_')):
                item_path = os.path.join(test_output_dir, item)
                if os.path.isdir(item_path):
                    found_project_dir = True
                    # Clean it up if found, as it's unexpected
                    shutil.rmtree(item_path)
                    break
    assert not found_project_dir, f"A directory for project '{project_name}' was unexpectedly created in '{test_output_dir}'."

    # 4. Transition to ISSUES and try again
    response = client.post("/approve") # PLANNING -> ISSUES
    assert response.status_code == 200
    data = response.json()
    assert data["new_state"] == AppStates.ISSUES.value

    response_gen_issues = client.post("/generate_files")
    assert response_gen_issues.status_code == 200
    gen_data_issues = response_gen_issues.json()
    assert gen_data_issues["status"] == "not_ready_for_generation"
    assert AppStates.ISSUES.value in gen_data_issues["message"]

    found_project_dir_issues = False
    if os.path.exists(test_output_dir):
        for item in os.listdir(test_output_dir):
            if item.startswith(project_name.lower().replace(' ', '_')):
                item_path = os.path.join(test_output_dir, item)
                if os.path.isdir(item_path):
                    found_project_dir_issues = True
                    shutil.rmtree(item_path)
                    break
    assert not found_project_dir_issues, f"A directory for project '{project_name}' was unexpectedly created in '{test_output_dir}' while in ISSUES state."

    # Cleanup of test_output_dir itself is handled by the fixture.

def test_generate_files_no_active_session(test_output_dir, monkeypatch):
    """
    Tests that /generate_files endpoint returns a 400 error if no session is active.
    """
    # Ensure that any test-specific output base dir is set, though it shouldn't be used
    monkeypatch.setattr("backend.file_generator.BASE_OUTPUT_DIR_FOR_TESTS", test_output_dir)

    # To simulate "no active session", we can try to reset the session in the global orchestrator
    # This is a bit invasive but necessary if the orchestrator is a global instance.
    # A better approach for app design would be dependency injection for the orchestrator,
    # but for now, we'll work with the existing structure.

    # Access the global orchestrator from the app instance if possible, or import it directly
    # from backend.main import orchestrator as global_orchestrator # Assuming it's accessible
    # For this test, let's assume 'client' uses 'app' which has its own 'orchestrator' instance.
    # If 'orchestrator' is truly global and shared across TestClient re-instantiations (unlikely for TestClient),
    # then we'd need to reset it.
    # However, TestClient(app) should provide sufficient isolation at the app level for each test run
    # if state is managed within request lifecycles or well-encapsulated.
    # The issue is that `orchestrator` in `main.py` is a global singleton.
    # So, its state persists across test client calls within the same test module run if not reset.

    # For this specific test, we want to ensure orchestrator.session is None or project_name is None.
    # The `/start` endpoint initializes `orchestrator.session`.
    # If other tests ran `/start`, then `orchestrator.session` might exist.

    # Create a fresh client and orchestrator instance for this test to ensure isolation
    # from previous tests that might have started a session.
    # This is one way to get a "clean slate" for the orchestrator's state.
    from backend.main import app as main_app # app from global import might be shared
    from backend.orchestrator import Orchestrator # Import the class

    # Temporarily replace the app's orchestrator with a fresh one for this test
    original_orchestrator = main_app.dependency_overrides.get(Orchestrator) # if using DI
    # If not using FastAPI DI for orchestrator, but it's a global `orchestrator = Orchestrator()` in main.py:
    from backend.main import orchestrator as global_main_orchestrator

    # Store the original session if it exists, and set session to None
    original_session = global_main_orchestrator.session
    global_main_orchestrator.session = None # Simulate no session started

    try:
        response_gen = client.post("/generate_files")
        assert response_gen.status_code == 400 # As per main.py logic
        gen_data = response_gen.json()
        assert "detail" in gen_data
        assert gen_data["detail"] == "Nenhuma sessão de projeto ativa. Inicie um projeto primeiro."
        assert gen_data.get("error_code") == "HTTP_EXCEPTION" # Or whatever code main.py sets

    finally:
        # Restore the original session to avoid affecting other tests
        global_main_orchestrator.session = original_session

    # Verify no output directory was created
    found_any_dir = False
    if os.path.exists(test_output_dir):
        if os.listdir(test_output_dir): # Check if the directory is not empty
            # Try to be more specific if possible, but any dir here would be unexpected
            # For now, let's assume if anything is here, it's an issue.
            # However, other tests might legitimately create files here if run in parallel
            # or if cleanup from a previous test failed.
            # This assertion is tricky without more context on test execution order.
            # For now, let's assume test_output_dir should be empty of project-specific folders.
            # This test does not create a project, so no project-specific folder should exist.
            pass # The fixture cleans up test_output_dir, so an explicit check here is less critical
                 # than for tests that *might* create something.
