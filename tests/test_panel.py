import sys
import os

# Ensure repository root is in PYTHONPATH for CI environments
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pandas as pd
from analysis.generate_repo_panel import generate_repo_panel

def test_panel_structure():
    import numpy as np
    np.random.seed(42)
    df = generate_repo_panel(n_repos=5, n_months=3)

    required_cols = [
        "repo_id", "month", "downloads", "reuse_events",
        "reuse_rate", "adapt_latency", "Lg", "contributor_growth",
        "age_months", "org_flag", "modality"
    ]

    for col in required_cols:
        assert col in df.columns, f"Missing column: {col}"

    assert len(df) == 15, "n_repos * n_months rows expected"
    assert df["downloads"].min() > 0