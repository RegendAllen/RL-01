
# gymnasium入门


import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')

env.reset()
print(env.reset())

env.action_space
print(env.action_space)

env.render()

plt.imshow(env.render())
plt.show()  # 调用show方法才能显示


# 另一段示例，显示随机动作和状态
env.reset()
action = env.action_space.sample()
print(action)
state, reward, terminated, trucated, info = env.step(action)
print(state)


