import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
env = gym.make('NChain-v0')
env.reset()
out = env.step(1)
print(out)
out = env.step(0)
print(out)
out = env.step(0)
print(out)
out = env.step(0)
print(out)
out = env.step(0)
print(out)