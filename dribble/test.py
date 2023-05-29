import rlgym
import time
from dribble_state import DribbleState
from rlgym.utils.terminal_conditions import common_conditions
from ball_fell_condition import BallFellCondition
env = rlgym.make(state_setter = DribbleState(),
				terminal_conditions=[common_conditions.TimeoutCondition(225),BallFellCondition()],
				game_speed=2,spawn_opponents=False,team_size=1,raise_on_crash=True)


while True:
	obs = env.reset()
	done = False

	while not done:
	  #Here we sample a random action. If you have an agent, you would get an action from it here.
	  action = env.action_space.sample()
	  action -= action
	  
	  next_obs, reward, done, gameinfo = env.step(action)
	  
	  obs = next_obs

