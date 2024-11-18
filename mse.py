from typing import List

from rem_base import BaseREM


class MSE(BaseREM):

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

    def square_errors(self):
        squ_errs = []
        for e in self.errors:
            squ_errs.append(pow(e, 2))
        self.errors = squ_errs
