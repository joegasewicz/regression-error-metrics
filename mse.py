from typing import List

from rem_base import BaseREM


class MSE(BaseREM):
    """
    The most popular choice of evaluation error because it punishes
    larger errors.
    """

    def __init__(self, *,
                 actual_vals: List[int],
                 predicted_vals: List[int],
                 ):
        """
        The Mean Squared Error penalizes larger errors more heavily by squaring them,
        making it more sensitive to outliers.
        """
        super().__init__(
            actual_vals=actual_vals,
            predicted_vals=predicted_vals,
        )
