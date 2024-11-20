from typing import List
import math

from rem_base import BaseREM


class RMSE(BaseREM):
    """
    More popular than MSE because RMSE is interpretable in the y units.
    """

    square_root: float

    def __init__(self, *,
                 actual_vals: List[int],
                 predicted_vals: List[int],
                 ):
        super().__init__(
            actual_vals=actual_vals,
            predicted_vals=predicted_vals,
        )
        self.square_root = 0

    def set_mean(self) -> None:
        self.square_root = self.get_mean()

    def get_square_root(self) -> float:
        return math.sqrt(self.square_root)
