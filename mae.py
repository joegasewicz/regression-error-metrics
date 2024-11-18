from typing import List


class MAE:
    actual_vals: List[int]
    predicted_vals: List[int]
    errors: List[int]
    result: int
    n: int # absolute number of data points

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

    def calc_errors(self):
        range_len = len(self.actual_vals)
        for i in range(range_len):
            self.errors.append(self.actual_vals[i]-self.predicted_vals[i])

    def set_absolute_vals(self):
        abs_errors = []
        for e in self.errors:
            abs_errors.append(abs(e))
        self.errors = []
        self.errors = abs_errors

    def sum_abs_errors(self):
        for e in self.errors:
            self.result += e

    def get_mean(self):
        return self.result/self.n
