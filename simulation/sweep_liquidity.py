import numpy as np
from env_liquidity import LiquidityEnv
import pandas as pd
import json
import os

def load_config():
    cfg_path = os.path.join("..", "configs", "sim_config.json")
    if os.path.exists(cfg_path):
        with open(cfg_path, "r") as f:
            return json.load(f)
    return None

def run_sweep(connectivities, seeds):
    rows = []

    for L in connectivities:
        eff_list = []

        for s in seeds:
            np.random.seed(s)
            env = LiquidityEnv(n_agents=100, base_connectivity=L)
            obs = env.reset()

            done = False
            while not done:
                actions = np.random.randint(0, 4, env.n_agents)
                obs, reward, done, info = env.step(actions)

            eff_list.append(np.mean(env.global_efficiency))

        rows.append({
            "L": p,
            "efficiency": np.mean(eff_list),
            "stddev": np.std(eff_list),
            "notes": ""
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    cfg = load_config()

    if cfg is not None:
        start = cfg.get("sweep_start", 0.10)
        end = cfg.get("sweep_end", 0.95)
        points = cfg.get("sweep_points", 15)
        seeds = cfg.get("seeds", [42, 123, 888, 2025, 9001])
        output = cfg.get("sweep_output", "../data/liquidity_efficiency_curve.csv")
    else:
        start, end, points = 0.10, 0.95, 15
        seeds = [42, 123, 888, 2025, 9001]
        output = "../data/liquidity_efficiency_curve.csv"

    connectivities = np.linspace(start, end, points)

    df = run_sweep(connectivities, seeds)
    df.to_csv(output, index=False)
    print(f"Saved sweep results → {output}")