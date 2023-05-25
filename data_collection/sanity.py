import rlgym
from time import sleep
import numpy as np
import sys
import os
import pickle

import numpy as np
import torch

from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.utils.data import random_split

from torch import Tensor
from torch.nn import Linear
from torch.nn import SELU
from torch.nn import Tanh
from torch.nn import Module
from torch.nn import Dropout

from torch.nn import MSELoss
from torch.optim import Adam

from squared_obs import SquaredObs

class Net(Module):
    # define model elements
    def __init__(self):
        super().__init__()
        # input to first hidden layer
        n_inputs = 119
        
        self.dropout1 = Dropout(0.2)
        self.dropout2 = Dropout(0.2)
        
        self.hidden1 = Linear(n_inputs, 256)
        self.act1 = SELU()

        self.hidden2 = Linear(256, 256)
        self.act2 = SELU()

        self.hidden3 = Linear(256, 128)
        self.act3 = SELU()

        self.hidden4 = Linear(128, 64)
        self.act4 = SELU()
        
        # third hidden layer and output
        self.hidden5 = Linear(64, 8)
        self.act5 = Tanh()

    # forward propagate input
    def forward(self, X):
        # input to first hidden layer
        X = self.hidden1(X)
        X = self.act1(X)
         # second hidden layer
        X = self.hidden2(X)
        X = self.act2(X)
        
        X = self.dropout1(X)
        
        # third hidden layer and output
        X = self.hidden3(X)
        X = self.act3(X)
        
        X = self.dropout2(X)
        
        X = self.hidden4(X)
        X = self.act4(X)
        
        X = self.hidden5(X)
        X = self.act5(X)
        return X
model = Net()
paths = [float(x[:-4]) for x in os.listdir('models') if not x.startswith('.')]
best = min(paths)
model.load_state_dict(torch.load(f'models/{best:.6f}.pth'))

team_size = 2

env = rlgym.make(spawn_opponents=True,
				team_size=team_size,
				game_speed = 1,
				obs_builder = SquaredObs())
obs = env.reset()

initialized = False
game_info = None
model.eval()
while True:
	actions = []
	print(game_info)
	for i in range(team_size*2):
		if game_info == None:
			print("using random")
			action_i = env.action_space.sample()
		else:
			print("using Necto")
			action_i = model.forward(game_info['state'])
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