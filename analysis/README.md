# Analysis Module

This folder contains scripts for constructing the synthetic repo–month panel
and running the quadratic regression that produces the inverted-U relationship
between liquidity and efficiency.

### Files

- **generate_repo_panel.py**  
  Generates a synthetic panel consistent with the paper.

- **run_regression.py**  
  Runs an OLS quadratic regression over Lg to produce beta coefficients and
  the turning point L*.

- **regression_results.ipynb**  
  Notebook demonstrating regression analysis interactively.

### Usage
<code>python generate_repo_panel.py
</code>
<code>python run_regression.py
</code>