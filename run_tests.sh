#!/bin/bash

# 1. Fail immediately if any command fails, undefined variables exist, or pipes fail
set -euo pipefail

echo "--- Starting CI Test Engine ---"

# 2. Virtual Environment Setup
# Keeps the CI environment clean
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
# Ensure pytest and pytest-dash are installed
pip install pytest pytest-dash selenium webdriver-manager

# 4. Environment Sanity Check
# Make sure the data file exists before starting the app
if [ ! -f "data/pink_morsels_sales.csv" ]; then
    echo "ERROR: Data file not found at data/pink_morsels_sales.csv"
    exit 1
fi

# 5. Execute Tests
# We run pytest. dash_duo will handle starting/stopping the server.
# --headless is crucial for CI environments without a GUI.
echo "Running integration tests..."
pytest tests/test.py --webdriver Chrome --headless

# 6. Capture the exit code of pytest
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "--- TESTS PASSED ---"
    exit 0
else
    echo "--- TESTS FAILED ---"
    exit 1
fi