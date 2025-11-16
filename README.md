# Agentic Liquidity: Code, Data, and Simulation Environment

This repository contains the full codebase, data pipeline, and simulation framework
used in the paper *Agentic Liquidity: Economic Modeling of Interoperability and Systemic Risk in AI Ecosystems*.

It includes:

- A repo–month panel generator for Hugging Face / ModelScope style data
- Quadratic regression reproducing the inverted-U relationship
- A liquidity-driven multi-agent simulation environment
- A sweep script producing the liquidity–efficiency curve
- Config files, seeds, and reproducible scripts
- Unit tests and notebooks for replication

## Repository Structure
analysis /    – panel
construction + regression
simulation /  – liquidity
environment + sweep
data /        – sample
datasets + curves
configs /     – JSON
configs + seeds
tests /       – basic
unit
tests
## Installation
pip install -r requirements.txt
## Reproducing the Results

### 1. Generate the repo–month panel
python analysis/generate_repo_panel.py
### 2. Run the regression
python analysis/run_regression.py
### 3. Run the liquidity sweep
python simulation/sweep_liquidity.py
## Citation

If you use this code, please cite the paper.
