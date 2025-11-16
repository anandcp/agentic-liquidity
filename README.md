<p align="left">
  <a href="https://github.com/anandcp/agentic-liquidity/actions">
    <img src="https://github.com/anandcp/agentic-liquidity/actions/workflows/test.yml/badge.svg" alt="CI Status">
  </a>
  <a href="https://github.com/anandcp/agentic-liquidity/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/anandcp/agentic-liquidity" alt="License: MIT">
  </a>
  <a href="https://github.com/anandcp/agentic-liquidity/stargazers">
    <img src="https://img.shields.io/github/stars/anandcp/agentic-liquidity?style=social" alt="Stars">
  </a>
</p>

# Agentic Liquidity: Code, Data, and Simulation Environment

This repository contains the full codebase, data pipeline, and simulation framework
used in the paper *Agentic Liquidity: Economic Modeling of Interoperability and Systemic Risk in AI Ecosystems*.

It provides:

- A synthetic repo–month panel generator for model‑hub style datasets  
- A quadratic regression pipeline reproducing the inverted‑U liquidity–efficiency curve  
- A liquidity‑driven multi‑agent simulation environment  
- A sweep script that generates the full liquidity–efficiency dataset  
- Configuration files, seeds, notebooks, and unit tests for reproducibility  
- GitHub Actions CI for automated validation

---

## Repository Structure

```
analysis/     – repo panel generator + regression scripts
simulation/   – liquidity environment + sweep + notebooks
data/         – sample datasets + synthetic curves
configs/      – JSON configs + seeds
tests/        – basic unit tests for env, panel, and regression
```

---

## Installation

```
pip install -r requirements.txt
```

(Optional) activate your virtual environment before installing dependencies.

---

## Reproducing the Results

### 1. Generate the repo–month panel

```
python analysis/generate_repo_panel.py
```

### 2. Run the regression

```
python analysis/run_regression.py
```

### 3. Run the liquidity sweep

```
python simulation/sweep_liquidity.py
```

### 4. Run all steps automatically

```
./run_all.sh
```

---

## Unit Tests

To run the full test suite:

```
pytest -q
```

---

## Notebooks

Interactive notebooks for regression and simulation are located in:

```
analysis/regression_results.ipynb
simulation/sim_results.ipynb
```

Open them in PyCharm or VS Code with the Jupyter plugin enabled.

---

## Citation

If you use this code, please cite:

**Pranatharthy Codangudi, A. (2025).  
Agentic Liquidity: Economic Modeling of Interoperability and Systemic Risk in AI Ecosystems.**

The CITATION.cff file in this repository provides full citation metadata.

---

## License

This project is released under the MIT License. See the `LICENSE` file for details.
