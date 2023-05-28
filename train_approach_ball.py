# Here we import the Match object and our multi-instance wrapper
from rlgym.envs import Match
from rlgym_tools.sb3_utils import SB3MultipleInstanceEnv
import os
# Since we can't use the normal rlgym.make() function, we need to import all the default configuration objects to give to our Match.
from custom_reward import CustomReward
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.state_setters import DefaultState
from rlgym.utils.action_parsers import DefaultAction
from rlgym.utils.reward_functions.combined_reward import CombinedReward
from rlgym.utils.terminal_conditions.common_conditions import *
from rlgym.utils.reward_functions.common_rewards import *
from rlgym_tools.extra_rewards.diff_reward import DiffReward
from rewards.grounded_reward import GroundedReward
from rewards.linear_ball_dist import LinearDistReward


# Finally, we import the SB3 implementation of PPO.
from stable_baselines3.ppo import PPO

# This is the function we need to provide to our SB3MultipleInstanceEnv to construct a match. Note that this function MUST return a Match object.
def get_match():
	
	# Here we configure our Match. If you want to use custom configuration objects, make sure to replace the default arguments here with instances of the objects you want.
	return Match(
		CombinedReward.from_zipped(
			(LiuDistancePlayerToBallReward(), 5),
			(LiuDistanceBallToGoalReward(), 10),
			(FaceBallReward(),2),
			(GroundedReward(), .1),
			# (LinearDistReward()),
			(ConstantReward(),-8.875),
			(EventReward(touch=3, team_goal=30, concede=-30)),
		),
		(GoalScoredCondition(), TimeoutCondition(1500)),
		DefaultObs(),
		DefaultAction(),
		DefaultState(),
		spawn_opponents=True,
	)
	

#If we want to spawn new processes, we have to make sure our program starts in a proper Python entry point.
if __name__ == "__main__":
	"""
		Now all we have to do is make an instance of the SB3MultipleInstanceEnv and pass it our get_match function, the number of instances we'd like to open, and how long it should wait between instances.
		This wait_time argument is important because if multiple Rocket League clients are opened in quick succession, they will cause each other to crash. The exact reason this happens is unknown to us,
		but the easiest solution is to delay for some period of time between launching clients. The amount of required delay will depend on your hardware, so make sure to change this number if your Rocket League
		clients are crashing before they fully launch.
	"""
	env = SB3MultipleInstanceEnv(match_func_or_matches=get_match, num_instances=3, wait_time=10)
	model = PPO(policy="MlpPolicy", env=env, verbose=1,
				learning_rate = 1e-3, batch_size = 128,
				gamma=1)
	try:
		models = [int(x[:-4]) for x in os.listdir("models") if x[-3:]=='zip']
		latest = max(models)
		loaded_model = PPO.load(f"models/{latest}")
		model.policy = loaded_model.policy
		step = latest
		print("loaded model",latest)
	except:
		print("existing model not detected, loading new model")
		# model = PPO(policy="MlpPolicy", env=env, verbose=1,
		# 		learning_rate = 1e-3, batch_size = 128,
		# 		gamma=1)
		step = 0
	step_size = 200_000
	while True:
		model.learn(step_size)
		step+=step_size
		model.save(f"models/{step}")