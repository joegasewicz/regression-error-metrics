from mse import MSE


class TestMSE:

    def test_new(self):
        mse = MSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        assert isinstance(mse, MSE)

    def test_calc_errors(self):
        mse = MSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mse.calc_errors()
        assert mse.errors == [-1, 1, -1]

        mse2 = MSE(
            actual_vals=[   34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        mse2.calc_errors()
        assert mse2.errors == [-3, -3, -2, 3, 2, -2, 1, -1, -2, -3, 4, 1]

    def test_square_errors(self):
        mse = MSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mse.calc_errors()
        mse.square_errors()
        assert len(mse.errors) == len(mse.actual_vals)
        assert mse.errors == [1, 1, 1]

        mse2 = MSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        mse2.calc_errors()
        mse2.square_errors()
        assert len(mse.errors) == len(mse.actual_vals)
        assert mse2.errors == [9, 9, 4, 9, 4, 4, 1, 1, 4, 9, 16, 1]

    def test_sum_errors(self):
        mse = MSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mse.calc_errors()
        mse.square_errors()
        mse.sum_errors()
        assert mse.result == 3

        mse2 = MSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        mse2.calc_errors()
        mse2.square_errors()
        mse2.sum_errors()
        assert mse2.result == 71

    def test_get_mean(self):
        mse = MSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mse.calc_errors()
        mse.square_errors()
        mse.sum_errors()
        result = mse.get_mean()
        assert result == 1

        mse2 = MSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        mse2.calc_errors()
        mse2.square_errors()
        mse2.sum_errors()
        result2 = mse2.get_mean()
        assert round(result2, 5) == 5.91667
