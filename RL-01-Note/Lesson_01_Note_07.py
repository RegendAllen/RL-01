

# 防止陷入循环状态的示例
# 在某些情况下，动作和状态会陷入到死循环中，这时并不需要再记录状态及进行下去，
# 所以需要对上一笔记中的记录value的代码进行修改


import gymnasium as gym
import matplotlib.pyplot as plt
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 10000

state, info = env.reset()

trajectories = []

for _ in tqdm(range(episode)):
    trajectory = []
    while True:
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)

        trajectory.append((state, action, reward))

        state = next_state

        if terminated or truncated:
            state, info = env.reset()

            trajectories.append(trajectory)

            break

env.close()

print(trajectories)
print('one sample of trajectories : ')
print(trajectories[2])


# 用蒙特卡罗方法求value
import numpy as np
from collections import defaultdict

G = 0  # 单步reward
gamma = 0.9
value = defaultdict(list)  # value（state）


for t in trajectories:

    visited = set()  # 在每一步中
    for (s, a, r) in t[::-1]:
        if s not in visited:  # 只添加新的，见过的不添加，即不要循环
            G = r + gamma * G
            value[s].append(G)
            visited.add(s)
            # print(value)


for s, g in value.items():
    value[s] = np.mean(g)

print(value)



# 分析牌局发现，需要分类统计牌局中有没有A的情况
# 分析value的组成情况（将牌局分为有A和没有A两种情况分析）
value_with_ace = np.zeros((20+10, 11))  # 观察到的值，玩家最大是20+10，庄家最大是A即11
value_with_ace[:] = np.nan
value_without_ace = np.zeros((20+10, 11))
value_without_ace[:] = np.nan

for(p, d, a), v in value.items():
    if a:
        value_with_ace[p][d] = v
    else:
        value_without_ace[p][d] = v

# print(value_with_ace)
# print(value_without_ace)

s1_value = plt.imshow(value_with_ace)
plt.xlabel('Dealer Show')
plt.ylabel('Player Show')
plt.colorbar(s1_value)
plt.show()

s2_value = plt.imshow(value_without_ace)
plt.xlabel('Dealer Show')
plt.ylabel('Player Show')
plt.colorbar(s2_value)
plt.show()
