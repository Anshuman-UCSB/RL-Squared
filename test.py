import rlgym
from time import sleep
import numpy as np
import sys
sys.path.insert(0, "nexto")
from bot import Nexto

import pickle

n1 = Nexto("stolen",0,0)
n2 = Nexto("stolen1",1,1)
n1.initialize_agent()
n2.initialize_agent()
team_size = 1

bots = [n1,n2]

env = rlgym.make(spawn_opponents=True,
				team_size=team_size,
				game_speed = 1)
obs = env.reset()

initialized = False

game_info = None

while True:
	actions = []
	for i in range(team_size*2):
		if game_info == None:
			print("using random")
			action_i = env.action_space.sample()
		else:
			print("using nexto")
			action_i = bots[i].forward(game_info['state'])
		# n.forward(obs)
		# sleep(1)
		actions.append(action_i)
	print(actions)
	obs, reward, done, game_info = env.step(actions)
		
	# 	with open('gs.txt', 'wb') as f:
	# 		pickle.dump((obs, reward, done, game_info), f)

f = pickle.load(open("gs.txt",'rb'))
gs = f[3]['state']
act = n.forward(gs)
def csToActions(cs):
	return [cs.throttle, cs.steer, cs.yaw, cs.pitch, cs.roll, int(cs.jump), int(cs.boost), int(cs.handbrake)]
print(act)