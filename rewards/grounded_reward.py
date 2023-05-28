from rlgym.utils import RewardFunction
from rlgym.utils.gamestates import PlayerData, GameState
import numpy as np

class GroundedReward(RewardFunction):
    """
    a ball touch reward that only triggers when the agent's wheels aren't in contact with the floor
    adjust minimum ball height required for reward with 'min_height' as well as reward scaling with 'exp'
    """

    def __init__(self):
        ...
    def reset(self, initial_state: GameState):
        pass

    def get_reward(
            self, player: PlayerData, state: GameState, previous_action: np.ndarray
            ) -> float:
        return int(player.on_ground)
        # return -player.car_data.position[2]
        # return -player.car_data.position[2]