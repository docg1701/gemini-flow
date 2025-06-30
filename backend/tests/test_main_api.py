import os
import pytest
from fastapi.testclient import TestClient
from backend.main import app # Main FastAPI application
from backend.orchestrator import AppStates, PROMPTS_DIR, PROMPT_FILES

# Create a TestClient instance using the FastAPI app
# This client will allow us to make requests to the application in our tests
client = TestClient(app)

# Store the original GEMINI_API_KEY to restore it after tests
# This is important if tests modify environment variables
_original_gemini_key = os.environ.get("GEMINI_API_KEY")

@pytest.fixture(autouse=True)
def setup_and_teardown_env():
    """
    Fixture to set up a dummy GEMINI_API_KEY for tests if not already set,
    and ensure prompt files are accessible.
    It also cleans up by restoring the original GEMINI_API_KEY.
    """
    # Ensure a dummy API key is set for the config to load,
    # as the app initialization depends on it.
    # The backend/config.py expects a .env file or environment variables.
    # For testing, we can directly set the environment variable if the .env
    # used by `decouple` in config.py isn't providing it during test discovery.
    # The TestClient runs the app in the same process, so config.py will be executed.
    # We want to ensure that `settings.GEMINI_API_KEY` is populated.
    # The current backend/.env has "YOUR_API_KEY_HERE"
    # If we want to override for tests, we can:
    # os.environ["GEMINI_API_KEY"] = "TEST_KEY_FROM_ENV_VAR"
    # print(f"[DEBUG test_main_api] Original GEMINI_API_KEY from env: {_original_gemini_key}")
    # print(f"[DEBUG test_main_api] Current GEMINI_API_KEY from env before test: {os.environ.get('GEMINI_API_KEY')}")
    # print(f"[DEBUG test_main_api] backend/.env path: {os.path.abspath('backend/.env')}")
    # print(f"[DEBUG test_main_api] CWD for test: {os.getcwd()}")


    # Check if prompt files are accessible from the perspective of the test environment
    # This check helps diagnose issues if tests fail due to missing prompts
    for state, filename in PROMPT_FILES.items():
        filepath = os.path.join(PROMPTS_DIR, filename)
        assert os.path.exists(filepath), \
            f"Prompt file for state {state.name} ({filename}) not found at {filepath}. PROMPTS_DIR: {PROMPTS_DIR}, CWD: {os.getcwd()}"

    yield  # This is where the testing happens

    # Teardown: restore original environment variable if it was changed
    # if _original_gemini_key is None:
    #     if "GEMINI_API_KEY" in os.environ:
    #         del os.environ["GEMINI_API_KEY"]
    # else:
    #     os.environ["GEMINI_API_KEY"] = _original_gemini_key
    # print(f"[DEBUG test_main_api] GEMINI_API_KEY restored to: {os.environ.get('GEMINI_API_KEY')}")


def test_health_check():
    """Test the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "healthy"
    assert "version" in json_response

def test_start_session():
    """Test the /start endpoint."""
    project_name = "Test Project Alpha"
    response = client.post("/start", json={"project_name": project_name})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "session_started"
    assert json_response["project_name"] == project_name
    assert json_response["current_state"] == AppStates.PLANNING.value
    assert "message" in json_response # Initial AI interaction
    # Check that the orchestrator's session was updated
    # This is an indirect check, relying on subsequent calls or direct inspection if possible
    # For now, we assume the response is authoritative.

def test_chat_endpoint_after_start():
    """Test the /chat endpoint after a session has been started."""
    # Start a session first
    client.post("/start", json={"project_name": "Chat Test Project"})

    user_message = "Este é meu primeiro comando."
    response = client.post("/chat", json={"user_message": user_message})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["user_message"] == user_message
    assert "ai_response" in json_response
    assert json_response["current_state"] == AppStates.PLANNING.value # Should still be in PLANNING
    assert json_response["history_length"] > 0 # History should have at least user + AI
    assert "is_approval_step" in json_response
    # Further checks on ai_response content could be done if we had a deterministic mock LLM

def test_approve_phase_planning_to_issues():
    """Test the /approve endpoint to move from PLANNING to ISSUES."""
    # 1. Start a session (defaults to PLANNING)
    client.post("/start", json={"project_name": "Approval Test Project 1"})

    # 2. Approve the current phase (PLANNING)
    response = client.post("/approve")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "state_changed"
    assert json_response["new_state"] == AppStates.ISSUES.value
    assert "message" in json_response # Should contain the initial AI message for the ISSUES phase

    # 3. (Optional) Send a chat message to confirm the state in orchestrator
    chat_response = client.post("/chat", json={"user_message": "Estamos na fase de issues?"})
    assert chat_response.status_code == 200
    chat_json = chat_response.json()
    assert chat_json["current_state"] == AppStates.ISSUES.value

def test_approve_phase_issues_to_devops():
    """Test the /approve endpoint to move from ISSUES to DEVOPS."""
    # 1. Start & move to ISSUES
    client.post("/start", json={"project_name": "Approval Test Project 2"})
    client.post("/approve") # PLANNING -> ISSUES

    # 2. Approve current phase (ISSUES)
    response = client.post("/approve")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "state_changed"
    assert json_response["new_state"] == AppStates.DEVOPS.value
    assert "message" in json_response

def test_approve_phase_devops_to_generate():
    """Test approving DEVOPS phase, making it ready for generation."""
    # 1. Start & move to DEVOPS
    client.post("/start", json={"project_name": "Approval Test Project 3"})
    client.post("/approve") # PLANNING -> ISSUES
    client.post("/approve") # ISSUES -> DEVOPS

    # 2. Approve current phase (DEVOPS)
    response = client.post("/approve")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "phase_approved_ready_to_generate"
    assert json_response["new_state"] == AppStates.DEVOPS.value # Stays in DEVOPS, but flagged as ready
    assert "message" in json_response

def test_generate_files_not_ready():
    """Test /generate_files when not in the final approved DEVOPS state."""
    client.post("/start", json={"project_name": "Generate Test Not Ready"})
    client.post("/approve") # PLANNING -> ISSUES

    response = client.post("/generate_files")
    assert response.status_code == 200 # The endpoint itself doesn't error, but returns a specific status
    json_response = response.json()
    assert json_response["status"] == "not_ready_for_generation"
    assert "message" in json_response

def test_generate_files_ready():
    """Test /generate_files when ready (after DEVOPS approved)."""
    # 1. Start & move through all approvals
    project_name = "Generate Test Ready"
    client.post("/start", json={"project_name": project_name})
    client.post("/approve") # PLANNING -> ISSUES
    client.post("/approve") # ISSUES -> DEVOPS
    client.post("/approve") # Approve DEVOPS, ready for generation

    # 2. Generate files
    response = client.post("/generate_files")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "files_generated_successfully"
    assert project_name in json_response["message"]

# More tests could be added:
# - Test for /chat before /start (should ideally fail or return specific message)
# - Test for /approve before /start
# - Test for /generate_files before /start
# - Test invalid request bodies (e.g., missing project_name in /start)
#   FastAPI handles this with 422 Unprocessable Entity, which TestClient will report.

def test_start_missing_project_name():
    """Test /start with missing project_name in request body."""
    response = client.post("/start", json={}) # Missing project_name
    assert response.status_code == 422 # Unprocessable Entity

def test_chat_missing_user_message():
    """Test /chat with missing user_message in request body."""
    client.post("/start", json={"project_name": "Test Project Beta"}) # Need to start session
    response = client.post("/chat", json={}) # Missing user_message
    assert response.status_code == 422

# Note: The `autouse=True` fixture `setup_and_teardown_env` ensures that for each test,
# the environment (like prompt file checks) is verified.
# The TestClient re-initializes the app or a version of it for each test or session,
# so state between tests that rely on the global `orchestrator` instance in `main.py`
# will be reset if the TestClient manages that lifecycle properly.
# If the orchestrator instance were a dependency injected per request, state management would be cleaner.
# Given the current structure (global orchestrator in main.py),
# the TestClient reuses this instance across calls within a single test function.
# However, for separate test functions, TestClient might be starting "fresh" interactions
# with the app, effectively resetting or getting a new app instance context if FastAPI or Starlette
# does this internally for TestClient. If not, the global orchestrator's state
# *will* persist across different test_functions if they hit the same app instance.
# This is a common challenge with global state in web app testing.
# For this setup, it seems `client.post/get` calls within a single test function
# interact with the same orchestrator state.
# To ensure test isolation for stateful tests like these, it's often better to:
# 1. Create a new client = TestClient(app) inside each test function OR
# 2. Have a fixture that provides a fresh client for each test OR
# 3. Re-initialize the orchestrator's state explicitly at the start of relevant tests
#    (e.g., client.post("/start", ...)) which is what is being done here.
# The current approach of calling /start in most tests effectively resets the relevant state.

# Example of how to reset orchestrator state IF it were directly accessible and mutable by tests
# (This is not the current design, just for illustration)
# @pytest.fixture(autouse=True)
# def reset_orchestrator_state_fixture():
#     from backend.main import orchestrator # direct import
#     orchestrator.start_new_session("Default Test Project") # Reset before each test

# The current `setup_and_teardown_env` fixture primarily checks prompt files.
# The API key part is more about ensuring the app *can* load config, not about
# resetting it for each test, as `python-decouple` caches loaded config.
# The critical part for test isolation is that each test sequence starts with `/start`
# which re-initializes `orchestrator.session`.

def test_chat_is_approval_step_logic():
    """
    Tests the is_approval_step logic across different phases and message counts.
    """
    project_name = "ApprovalStepLogicTest"

    # 1. Start session (PLANNING)
    response = client.post("/start", json={"project_name": project_name})
    assert response.status_code == 200
    start_json = response.json()
    assert start_json["current_state"] == AppStates.PLANNING.value

    # First chat in PLANNING
    # Orchestrator.start_new_session -> process_user_message("Olá! Vamos começar...")
    # History: user, assistant (2 messages)
    # The response from /start *is* the first AI interaction.
    # To check is_approval_step, we need a /chat call or look at orchestrator internals.
    # Let's make a /chat call to check.
    chat_response = client.post("/chat", json={"user_message": "My first actual message in PLANNING."})
    assert chat_response.status_code == 200
    chat_json = chat_response.json()
    assert chat_json["current_state"] == AppStates.PLANNING.value
    assert chat_json["is_approval_step"] == False, "is_approval_step should be False in PLANNING"
    # History: start_user, start_ai, chat_user, chat_ai (4 messages)
    assert chat_json["history_length"] == 4

    # 2. Approve to ISSUES
    approve_to_issues_response = client.post("/approve")
    assert approve_to_issues_response.status_code == 200
    approve_to_issues_json = approve_to_issues_response.json()
    assert approve_to_issues_json["new_state"] == AppStates.ISSUES.value

    # The response from /approve includes the first AI message of the new phase.
    # This AI message is generated by process_user_message, which also calculates is_approval_step.
    # History after /approve to ISSUES:
    # - Initial 2 from /start's "Olá..." + user message in PLANNING (total 4 before this /approve)
    # - change_state to ISSUES: +1 system message (total 5)
    # - process_user_message for "Ok, aprovei...": +2 (user, assistant) (total 7)
    # Let's re-verify Orchestrator.process_user_message return structure for /approve
    # main.py: approve_phase -> orchestrator.process_user_message(...) -> returns dict with "is_approval_step"
    # However, ApproveResponse model in main.py does NOT include is_approval_step.
    # So we cannot check it from /approve response directly. We need a subsequent /chat.

    chat_in_issues_response = client.post("/chat", json={"user_message": "My first message in ISSUES."})
    assert chat_in_issues_response.status_code == 200
    chat_in_issues_json = chat_in_issues_response.json()
    assert chat_in_issues_json["current_state"] == AppStates.ISSUES.value
    assert chat_in_issues_json["is_approval_step"] == False, "is_approval_step should be False in ISSUES"
    # History:
    # Initial /start: "Olá!..." (user) + AI response (2)
    # /chat in PLANNING: "My first actual..." (user) + AI response (2) -> Total 4
    # /approve to ISSUES: session.change_state adds system message (1) -> Total 5. No explicit user/AI message pair here anymore.
    # /chat in ISSUES: "My first message..." (user) + AI response (2) -> Total 7
    assert chat_in_issues_json["history_length"] == 7

    # 3. Approve to DEVOPS
    approve_to_devops_response = client.post("/approve")
    assert approve_to_devops_response.status_code == 200
    approve_to_devops_json = approve_to_devops_response.json()
    assert approve_to_devops_json["new_state"] == AppStates.DEVOPS.value

    # Again, /approve response doesn't have is_approval_step. Check with a /chat.
    chat_in_devops_response1 = client.post("/chat", json={"user_message": "My first message in DEVOPS."})
    assert chat_in_devops_response1.status_code == 200
    chat_in_devops_json1 = chat_in_devops_response1.json()
    assert chat_in_devops_json1["current_state"] == AppStates.DEVOPS.value
    # History after /approve to DEVOPS:
    # - History before this /approve: 9
    # - change_state to DEVOPS: +1 system message (total 10)
        # - History from ISSUES phase was 7.
        # - /approve to DEVOPS: session.change_state adds system message (1) -> Total 7 + 1 = 8
    # Now, this chat_in_devops_response1:
        # - process_user_message for "My first message in DEVOPS.": +2 (user, assistant) -> Total 8 + 2 = 10
        # Current state is DEVOPS, history length is 10. 10 > 5 is True for is_approval_step.
    assert chat_in_devops_json1["is_approval_step"] == True, "is_approval_step should be True in DEVOPS after entering"
    assert chat_in_devops_json1["history_length"] == 10

    # Send a few more messages in DEVOPS to ensure it stays true
    chat_in_devops_response2 = client.post("/chat", json={"user_message": "My second message in DEVOPS."})
    assert chat_in_devops_response2.status_code == 200
    chat_in_devops_json2 = chat_in_devops_response2.json()
    assert chat_in_devops_json2["current_state"] == AppStates.DEVOPS.value
    assert chat_in_devops_json2["is_approval_step"] == True, "is_approval_step should remain True in DEVOPS"
    # History: 10 + 2 = 12
    assert chat_in_devops_json2["history_length"] == 12

    # Test the other condition for requires_approval: last AI message contains "[APROVAR AGORA]"
    # This requires mocking the AI response or having more control over the orchestrator.
    # For now, focusing on the history length in DEVOPS state.
    # The current mock AI response does not include "[APROVAR AGORA]".
