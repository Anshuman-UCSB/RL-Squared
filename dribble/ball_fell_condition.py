from rlgym.utils.terminal_conditions import TerminalCondition
from rlgym.utils.gamestates import GameState

class BallFellCondition(TerminalCondition):

	def __init__(self):
		super().__init__()
		self.last_touch = None

	def reset(self, initial_state: GameState):
		self.last_touch = initial_state.last_touch

	def is_terminal(self, current_state: GameState) -> bool:
		"""
		Return `True` if the last touch does not have the same ID as the last touch from the initial state.
		"""
		return current_state.ball.position[2]<110
