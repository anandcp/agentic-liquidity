import numpy as np
import pandas as pd
import os

rng = np.random.default_rng(42)

def generate_repo_panel(n_repos=20, n_months=6):
    repo_ids = [f"repo_{i:04d}" for i in range(n_repos)]
    months = pd.date_range("2023-01-01", periods=n_months, freq="MS")

    rows = []

    for rid in repo_ids:
        base_popularity = rng.integers(500, 15000)
        org_flag = rng.integers(0, 2)
        modality = rng.choice(["llm", "vision", "speech", "multimodal"])

        for t, dt in enumerate(months):
            downloads = int(base_popularity * (1 + 0.01 * t) * rng.normal(1.0, 0.2))
            downloads = max(downloads, 100)

            reuse_events = rng.poisson(lam=max(downloads / 1000, 0.5))
            reuse_rate = reuse_events / max(downloads / 1000, 1)

            adapt_latency = max(rng.normal(loc=12 - 0.3 * reuse_rate, scale=4), 0.5)

            Lg = reuse_rate / (adapt_latency + 1)

            growth = rng.normal(loc=0.02 * Lg, scale=0.03)

            rows.append({
                "repo_id": rid,
                "month": dt.strftime("%Y-%m"),
                "downloads": downloads,
                "reuse_events": reuse_events,
                "reuse_rate": reuse_rate,
                "adapt_latency": adapt_latency,
                "Lg": Lg,
                "contributor_growth": growth,
                "age_months": t + 1,
                "org_flag": org_flag,
                "modality": modality
            })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    df = generate_repo_panel()
    df.to_csv("../data/sample_repo_panel.csv", index=False)
    print("Generated panel at data/sample_repo_panel.csv")
    print(df.head())