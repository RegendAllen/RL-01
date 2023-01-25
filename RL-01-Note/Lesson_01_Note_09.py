

# 用随机方法玩21点，并统计胜率


import gymnasium as gym
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 20000

state, info = env.reset()

trajectories = []

win_or_lose = []  # 增加胜率统计

for _ in tqdm(range(episode)):
    trajectory = []
    while True:
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)

        trajectory.append((state, action, reward))

        state = next_state

        if terminated or truncated:
            if reward > 0:
                win_or_lose.append(1)
            else:
                win_or_lose.append(0)

            state, info = env.reset()

            trajectories.append(trajectory)

            break

env.close()

# print(trajectories)
# print('one sample of trajectories : ')
# print(trajectories[2])

win_percentage = sum(win_or_lose) / len(win_or_lose)
print(win_percentage)


