import rlgym
from Nexto.nexto_obs import NextoObsBuilder

env = rlgym.make(obs_builder = NextoObsBuilder(), game_speed=2,spawn_opponents=True,team_size=1,raise_on_crash=True)


it = 0
while it < 500:
	obs = env.reset()
	done = False

	while not done:
		it+=1
		if it >= 500:
			break
		print(it)
		#Here we sample a random action. If you have an agent, you would get an action from it here.
		action = env.action_space.sample()
		print(action)
		next_obs, reward, done, gameinfo = env.step([env.action_space.sample(),env.action_space.sample()])

		obs = next_obs
env.close()