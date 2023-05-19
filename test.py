import rlgym
from time import sleep
import numpy as np
import sys
sys.path.insert(0, "nexto")
from bot import Nexto

import pickle

n = Nexto("stolen",0,0,1,False,True,False)
n.initialize_agent()
team_size = 2
# env = rlgym.make(spawn_opponents=True,
# 				team_size=team_size,
# 				game_speed = 1)
# obs = env.reset()

# initialized = False

# while True:
# 	actions = []
# 	for i in range(team_size*2):
# 		# n.forward(obs)
# 		# sleep(1)
# 		action_i = env.action_space.sample()
# 		actions.append(action_i)
# 		obs, reward, done, game_info = env.step(actions)
# 		try:
# 			if not initialized:
# 				n.initialize_agent()
# 				initialized = True
# 			n.forward(game_info)
# 		except TypeError:
# 			print("still waiting for field_info")
		
# 	# 	with open('gs.txt', 'wb') as f:
# 	# 		pickle.dump((obs, reward, done, game_info), f)

f = pickle.load(open("gs.txt",'rb'))
gs = f[3]['state']
n.forward(gs)
print(gs)