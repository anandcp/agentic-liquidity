import numpy as np

class LiquidityEnv:
    """
    Minimal liquidity-driven multi-agent environment.
    Agents choose actions that affect throughput, latency, and synchronization.
    """

    def __init__(
        self,
        n_agents=100,
        base_connectivity=0.5,
        shock_prob=0.03,
        shock_duration=8,
        episode_len=150,
    ):
        self.n_agents = n_agents
        self.p = base_connectivity
        self.episode_len = episode_len
        self.shock_prob = shock_prob
        self.shock_duration = shock_duration

        self.t = 0
        self.shock_timer = 0

        # State variables
        self.queue = np.zeros(n_agents)
        self.throughput = np.zeros(n_agents)

        # Connectivity matrix (Erdos–Renyi)
        self.adj = (np.random.rand(n_agents, n_agents) < self.p).astype(float)
        np.fill_diagonal(self.adj, 0)

        # Metrics
        self.global_liquidity = []
        self.global_efficiency = []

    def reset(self):
        self.t = 0
        self.shock_timer = 0
        self.queue[:] = np.random.rand(self.n_agents) * 2
        self.throughput[:] = 0
        return self._get_obs()

    def _get_obs(self):
        """
        Observation vector: [queue_len, local_throughput, neighbor_flags, global_L]
        """
        neighbor_flags = (np.sum(self.adj, axis=1) > 0).astype(float)
        L = np.mean(neighbor_flags)  # simple proxy for demonstration

        obs = np.stack([
            self.queue,
            self.throughput,
            neighbor_flags,
            np.full(self.n_agents, L)
        ], axis=1)
        return obs

    def step(self, actions):
        """
        Actions:
        0 = replicate (increase load on neighbors)
        1 = throttle (reduce queue)
        2 = route (shift load to neighbors)
        3 = defer (do nothing)
        """
        # Apply shock
        if self.shock_timer > 0:
            shock_active = True
            self.shock_timer -= 1
        else:
            shock_active = False
            if np.random.rand() < self.shock_prob:
                self.shock_timer = self.shock_duration

        for i, a in enumerate(actions):
            if a == 0:  # replicate
                self.queue[i] += 0.5
                neighbors = np.where(self.adj[i] == 1)[0]
                if len(neighbors) > 0:
                    self.queue[neighbors] += 0.2

            elif a == 1:  # throttle
                self.queue[i] = max(self.queue[i] - 0.6, 0)

            elif a == 2:  # route
                neighbors = np.where(self.adj[i] == 1)[0]
                if len(neighbors) > 0:
                    routed = 0.3
                    self.queue[i] = max(self.queue[i] - routed, 0)
                    self.queue[neighbors] += routed / len(neighbors)

            elif a == 3:  # defer
                pass

        # Compute throughput
        self.throughput = np.where(self.queue > 0, 1.0 / (1.0 + self.queue), 1.0)

        # Efficiency: mean throughput with penalty for shocks
        efficiency = np.mean(self.throughput)
        if shock_active:
            efficiency *= 0.7

        # Liquidity proxy
        L = np.mean((np.sum(self.adj, axis=1) > 0).astype(float))

        self.global_liquidity.append(L)
        self.global_efficiency.append(efficiency)

        self.t += 1
        done = self.t >= self.episode_len

        return self._get_obs(), efficiency, done, {
            "liquidity": L,
            "efficiency": efficiency,
            "shock": shock_active
        }