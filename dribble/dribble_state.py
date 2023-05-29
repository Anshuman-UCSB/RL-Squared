from rlgym.utils.state_setters import StateSetter
from random import randint
from rlgym.utils.state_setters import StateWrapper
from rlgym.utils.math import rand_vec3
import numpy as np
from numpy import random as rand

# X_MAX = 7000
# Y_MAX = 9000
# Z_MAX_BALL = 1850
# Z_MAX_CAR = 1900
# PITCH_MAX = np.pi/2
# YAW_MAX = np.pi
# ROLL_MAX = np.pi


class DribbleState(StateSetter):

	def __init__(self):
		super().__init__()


	def reset(self, state_wrapper: StateWrapper):
		for car in state_wrapper.cars:
			car.set_pos(0,-2560,17)
			car.set_rot(yaw = 0.5 * np.pi)
		state_wrapper.ball.set_pos(0+randint(-3,10),-2560+randint(-10,10),150+randint(0,10))
