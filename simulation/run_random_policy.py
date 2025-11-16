from env_liquidity import LiquidityEnv
import numpy as np

env = LiquidityEnv()
obs = env.reset()

done = False
step = 0

while not done:
    actions = np.random.randint(0, 4, env.n_agents)
    obs, reward, done, info = env.step(actions)
    step += 1

print("Episode finished.")
print("Avg efficiency =", sum(env.global_efficiency) / len(env.global_efficiency))