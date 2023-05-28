from rlgym.utils import RewardFunction
from rlgym.utils.gamestates import PlayerData, GameState
import numpy as np

class LinearDistReward(RewardFunction):
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
        dist = np.linalg.norm(player.car_data.position - state.ball.position)
        return -dist  # Inspired by https://arxiv.org/abs/2105.12196
