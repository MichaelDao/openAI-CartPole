import gym
from gym import spaces

# set the gym as this game depending on whats passed
env = gym.make('CartPole-v0')

#print(env.action_spacei.high)
#> Discrete(2)
#print(env.observation_space.low)
#> Box(4,)

# set with 8 elements
space = spaces.Discrete(8) 

x = space.sample()

assert space.contains(x)
assert space.n == 8

# The process starts at this line
env.reset()

# 
for i_episode in range(20):
	observation = env.reset()

	for t in range(100):
		env.render()
		print (observation)
		action = env.action_space.sample()
	
		# Take a random action
	 	#env.step(env.action_space.sample())
 
		# object, float, boolean, dict
		observation, reward, done, info = env.step(action)
		
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			break
