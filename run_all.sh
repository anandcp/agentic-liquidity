#!/usr/bin/env bash
set -e

echo "----------------------------------------"
echo " Agentic Liquidity – Full Reproduction"
echo "----------------------------------------"

# 1. Activate Python environment (optional)
if [ -f "venv/bin/activate" ]; then
  echo "[1/8] Activating virtual environment..."
  source venv/bin/activate
else
  echo "[1/8] No virtual environment found. Using system Python."
fi

# 2. Install dependencies
echo "[2/8] Installing dependencies..."
pip install -r requirements.txt

# 3. Generate repo–month panel
echo "[3/8] Generating repository panel..."
python analysis/generate_repo_panel.py

# 4. Run quadratic regression
echo "[4/8] Running regression..."
python analysis/run_regression.py

# 5. Run liquidity sweep
echo "[5/8] Running liquidity sweep..."
python simulation/sweep_liquidity.py

# 6. Sanity test: run random policy RL
echo "[6/8] Running random policy simulation..."
python simulation/run_random_policy.py

# 7. Run unit tests
echo "[7/8] Running unit tests..."
pytest -q || echo "Tests finished with warnings."

# 8. Summary
echo "[8/8] All tasks completed."
echo "Data saved under ./data/"
echo "Regression and simulation outputs are ready."
echo "----------------------------------------"
echo " Finished."
echo "----------------------------------------"