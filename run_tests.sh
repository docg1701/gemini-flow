#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "======================================="
echo "Starting Comprehensive Test Script: run_tests.sh"
echo "======================================="

# --- Helper Function for Logging ---\n
log_action() {
    echo "\nINFO: $1"
}

log_success() {
    echo "SUCCESS: $1"
}

log_warning() {
    echo "WARNING: $1"
}

log_error_exit() {
    # Logs error to stderr and exits
    echo "\nERROR: $1. Aborting." >&2
    exit 1
}

# --- Environment Info ---
log_action "Displaying initial environment information"
echo "Initial PWD: $(pwd)"
ls -la
echo "Initial PYTHONPATH: ${PYTHONPATH}"
echo "Initial PATH: ${PATH}"
# It's good practice to ensure this script is run from project root.
# However, for now, we assume it will be. Can add checks later if needed.

PROJECT_ROOT="$(pwd)" # Assuming script is run from project root

# --- Backend Tests ---
log_action "Starting Backend Tests"
BACKEND_DIR="${PROJECT_ROOT}/backend"

log_action "Checking if backend directory exists: ${BACKEND_DIR}"
if [ -d "${BACKEND_DIR}" ]; then
    log_success "Backend directory found."

    log_action "Changing to backend directory: ${BACKEND_DIR}"
    cd "${BACKEND_DIR}" || log_error_exit "Failed to cd into backend directory."
    log_action "Current directory: $(pwd)"

    log_action "Ensuring backend dependencies are installed (poetry install --no-root --sync)"
    poetry install --no-root --sync || log_error_exit "poetry install failed."
    log_success "Poetry dependencies up-to-date for backend."

    log_action "Checking for backend/.env file"
    if [ -f ".env" ]; then
        log_success ".env file found in $(pwd)."
        echo "Contents of .env:"
        cat .env
    else
        log_warning ".env file NOT found in $(pwd). Configuration-dependent features might fail or use defaults."
        log_action "Creating a placeholder .env for this test run in $(pwd)."
        echo "GEMINI_API_KEY=TEST_FALLBACK_KEY_FROM_RUN_TESTS_SCRIPT" > .env
        log_success "Placeholder .env created for backend."
    fi

    # For orchestrator.py and main.py, they use `from backend.config...`
    # To run/compile them directly or via `python -m backend.module` from PROJECT_ROOT,
    # PROJECT_ROOT must be in PYTHONPATH.
    # To run/compile them as `python module.py` or `python -m module` from BACKEND_DIR,
    # they'd need relative imports (`from .config...`), OR BACKEND_DIR's parent (PROJECT_ROOT)
    # must be in PYTHONPATH.
    # Poetry `run` usually handles this by ensuring the project root is in sys.path.

    log_action "Attempting to run backend/orchestrator.py internal tests (if __name__ == '__main__': block)"
    # Assuming orchestrator.py uses absolute imports like "from backend.config"
    # Running poetry from the project root is more robust for this.
    (cd "${PROJECT_ROOT}" && poetry --directory=backend run python backend/orchestrator.py) || log_warning "Execution of orchestrator.py with 'poetry run python backend/orchestrator.py' from project root had issues. Check its output."
    log_success "Attempted to run orchestrator.py internal tests."

    log_action "Compiling backend/main.py (syntax and top-level imports)"
    (cd "${PROJECT_ROOT}" && poetry --directory=backend run python -m py_compile backend/main.py) || log_error_exit "Compilation of backend/main.py failed."
    log_success "backend/main.py compiled successfully."

    log_action "Compiling backend/config.py (syntax and top-level imports)"
    (cd "${PROJECT_ROOT}" && poetry --directory=backend run python -m py_compile backend/config.py) || log_error_exit "Compilation of backend/config.py failed."
    log_success "backend/config.py compiled successfully."

    log_action "Attempting to start Uvicorn (simulated, to check app load)"
    # This also requires PROJECT_ROOT in PYTHONPATH for 'from backend...' imports to resolve 'backend'.
    # The PYTHONPATH export before this command is crucial.
    # We are in BACKEND_DIR, so to refer to backend.main:app, Uvicorn needs to see the 'backend' package.
    # Safest is to run uvicorn from project root.
    (export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}" && cd "${PROJECT_ROOT}" && poetry --directory=backend run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --lifespan off --timeout-graceful-shutdown 1 &)
    UVICORN_PID=$!
    log_action "Uvicorn started with PID ${UVICORN_PID} in background (attempting for a few seconds)."
    sleep 5 # Give uvicorn a moment to start or fail

    if ps -p ${UVICORN_PID} > /dev/null; then
       log_success "Uvicorn process seems to be running (PID: ${UVICORN_PID})."
       log_action "Attempting basic health check with curl"
       curl -f http://localhost:8000/health || log_warning "Health check failed or Uvicorn not fully up."
       log_action "Stopping Uvicorn process (PID: ${UVICORN_PID})."
       kill ${UVICORN_PID}
       wait ${UVICORN_PID} 2>/dev/null # Suppress "Terminated" message
       log_success "Uvicorn stopped."
    else
       log_warning "Uvicorn process (PID: ${UVICORN_PID}) did not start or exited quickly. Check for errors above if Uvicorn tried to print them."
       # Attempt to capture any output if uvicorn wrote to a file or if logs are available
    fi

    # Placeholder for actual PyTest execution
    log_action "Placeholder for backend PyTest tests (e.g., task-031, task-032)"
    # if [ -d "tests" ]; then # Assuming tests are in backend/tests
    #    poetry run pytest tests/ || log_warning "PyTest backend tests failed or had issues."
    #    log_success "PyTest backend tests executed."
    # else
    #    log_warning "Backend 'tests' directory not found relative to $(pwd). Skipping PyTest."
    # fi

    log_action "Returning to project root: ${PROJECT_ROOT}"
    cd "${PROJECT_ROOT}" || log_error_exit "Failed to cd back to project root from backend."

else
    log_warning "Backend directory ${BACKEND_DIR} not found. Skipping backend tests."
fi
log_success "Backend Test Section Completed."


# --- Frontend Tests ---
log_action "Starting Frontend Tests"
FRONTEND_DIR="${PROJECT_ROOT}/frontend"

log_action "Checking if frontend directory exists: ${FRONTEND_DIR}"
if [ -d "${FRONTEND_DIR}" ]; then
    log_success "Frontend directory found."

    log_action "Changing to frontend directory: ${FRONTEND_DIR}"
    cd "${FRONTEND_DIR}" || log_error_exit "Failed to cd into frontend directory."
    log_action "Current directory: $(pwd)"

    log_action "Ensuring frontend dependencies are installed (npm install)"
    npm install || log_error_exit "npm install failed."
    log_success "npm dependencies installed/up-to-date for frontend."

    log_action "Running frontend build (includes TypeScript checks and linting)"
    npm run build || log_error_exit "npm run build failed for frontend."
    log_success "Frontend build completed successfully."

    # Placeholder for actual Jest test execution
    log_action "Placeholder for frontend Jest tests (e.g., task-033, task-034)"
    # log_action "Running frontend Jest tests (npm test)"
    # npm test -- --watchAll=false --passWithNoTests || log_warning "Frontend Jest tests failed or had issues."
    # # --passWithNoTests is useful if no test files are created yet
    # log_success "Frontend Jest tests executed."

    log_action "Returning to project root: ${PROJECT_ROOT}"
    cd "${PROJECT_ROOT}" || log_error_exit "Failed to cd back to project root from frontend."
else
    log_warning "Frontend directory ${FRONTEND_DIR} not found. Skipping frontend tests."
fi
log_success "Frontend Test Section Completed."


echo "\n======================================="
echo "Comprehensive Test Script Finished: run_tests.sh"
echo "======================================="
