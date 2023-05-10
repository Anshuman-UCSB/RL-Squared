import rlgym
import numpy as np

team_size = 3
env = rlgym.make(spawn_opponents=True,
				team_size=team_size)
try:
	obs = env.reset()

	while True:
		actions = []
		for i in range(team_size*2):
			action_i = env.action_space.sample()
			actions.append(action_i)
			new_obs, reward, done, game_info = env.step(actions)
except KeyboardInterrupt:
	env.close()