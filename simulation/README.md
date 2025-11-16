# Simulation Module

This module implements the liquidity-driven multi-agent environment used in the
paper *Agentic Liquidity: Economic Modeling of Interoperability and
Systemic Risk in AI Ecosystems*.

It includes:

- **env_liquidity.py**  
  The environment: agents observe local queues, neighbor signals,
  and global liquidity; they act by replicating, throttling, routing, or deferring load.

- **sweep_liquidity.py**  
  A sweep script that varies connectivity (p) and computes average efficiency,
  reward stability, and recovery time.

- **run_random_policy.py**  
  A minimal script to sanity-check the environment before running full PPO.

- **sim_results.ipynb**  
  Interactive notebook for exploring inverted-U patterns and recovery curves.

The environment is intentionally lightweight, avoiding heavy RL frameworks
so reviewers can reproduce results quickly.