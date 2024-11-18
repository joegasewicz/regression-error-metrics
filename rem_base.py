from abc import ABC
from typing import List


class BaseREM(ABC):
    actual_vals: List[int]
    predicted_vals: List[int]
    errors: List[int]
    result: int
    n: int  # absolute number of data points

    def __init__(self, *,
                 actual_vals: List[int],
                 predicted_vals: List[int],
                 ):
        self.actual_vals = actual_vals
        self.predicted_vals = predicted_vals
        if len(self.actual_vals) != len(self.predicted_vals):
            raise Exception("Actual & predicted lists must be the same length")
        self.result = 0
        self.errors = []
        self.n = len(self.actual_vals)

    def calc_errors(self) -> None:
        range_len = len(self.actual_vals)
        for i in range(range_len):
            self.errors.append(self.actual_vals[i]-self.predicted_vals[i])

    def square_errors(self):
        squ_errs = []
        for e in self.errors:
            squ_errs.append(pow(e, 2))
        self.errors = squ_errs

    def sum_errors(self) -> None:
        for e in self.errors:
            self.result += e

    def get_mean(self) -> float:
        """
        :return: Mean absolute error as a float
        """
        return self.result/self.n
