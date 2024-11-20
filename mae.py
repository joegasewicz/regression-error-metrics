from typing import List

from rem_base import BaseREM


class MAE(BaseREM):
    """
    The Mean Absolute Error measures the average absolute error,
    treating all errors equally. This evaluation metric is the easiest
    to understand.
    Takes the error to the absolute value of it & average it out.
    """

    def __init__(self, *,
                 actual_vals: List[int],
                 predicted_vals: List[int],
                 ):
        super().__init__(
            actual_vals=actual_vals,
            predicted_vals=predicted_vals,
        )

    def set_absolute_vals(self) -> None:
        abs_errors = []
        for e in self.errors:
            abs_errors.append(abs(e))
        self.errors = abs_errors
