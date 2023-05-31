from rlgym.utils.gamestates import GameState, PlayerData
from rlgym.utils.reward_functions import RewardFunction
import numpy as np 
class DribbleReward(RewardFunction):
    def reset(self, initial_state: GameState):
        pass

    def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        return 1 if state.ball.position[2] < 200 else 0