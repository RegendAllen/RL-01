

import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")
# ALE/Alien-v5      CartPole-v1     LunarLander-v2

env.reset()

env.render()
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    # state

    env.render()

    # done == terminated or truncated
    if terminated or truncated:
        observation, info = env.reset()

env.close()




