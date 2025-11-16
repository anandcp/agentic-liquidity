import sys
import os

# Ensure repository root is in PYTHONPATH for CI environments
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import numpy as np
from simulation.env_liquidity import LiquidityEnv

def test_env_basic_step():
    env = LiquidityEnv(n_agents=10, episode_len=20)
    obs = env.reset()

    assert obs.shape == (10, 4), "Observation shape must be (n_agents, 4)"

    actions = np.zeros(10, dtype=int)
    obs, reward, done, info = env.step(actions)

    assert "liquidity" in info
    assert "efficiency" in info
    assert isinstance(reward, float)

def test_env_terminates():
    env = LiquidityEnv(n_agents=5, episode_len=5)
    obs = env.reset()

    done = False
    step = 0

    while not done:
        actions = np.random.randint(0, 4, env.n_agents)
        obs, reward, done, info = env.step(actions)
        step += 1

    assert step == 5, "Environment should terminate exactly at episode_len"