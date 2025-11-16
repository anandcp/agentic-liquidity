import numpy as np
from env_liquidity import LiquidityEnv
import pandas as pd

def run_sweep(connectivities=np.linspace(0.1, 0.95, 15), seeds=5):
    rows = []

    for p in connectivities:
        eff_list = []

        for s in range(seeds):
            env = LiquidityEnv(n_agents=100, base_connectivity=p)
            obs = env.reset()

            done = False
            while not done:
                # random policy (replace with PPO for full version)
                actions = np.random.randint(0, 4, env.n_agents)
                obs, reward, done, info = env.step(actions)

            eff_list.append(np.mean(env.global_efficiency))

        rows.append({
            "p": p,
            "eff_mean": np.mean(eff_list),
            "eff_std": np.std(eff_list),
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = run_sweep()
    df.to_csv("../data/liquidity_efficiency_curve.csv", index=False)
    print("Saved sweep results → data/liquidity_efficiency_curve.csv")