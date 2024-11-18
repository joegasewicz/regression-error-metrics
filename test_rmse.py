from rmse import RMSE


class TestMAE:

    def test_new(self):
        rmse = RMSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        assert isinstance(rmse, RMSE)

    def test_calc_errors(self):
        rmse = RMSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        rmse.calc_errors()
        assert rmse.errors == [-1, 1, -1]

        rmse2 = RMSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        rmse2.calc_errors()
        assert rmse2.errors == [-3, -3, -2, 3, 2, -2, 1, -1, -2, -3, 4, 1]

    def test_square_errors(self):
        rmse = RMSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        rmse.calc_errors()
        rmse.square_errors()
        assert len(rmse.errors) == len(rmse.actual_vals)
        assert rmse.errors == [1, 1, 1]

        rmse2 = RMSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        rmse2.calc_errors()
        rmse2.square_errors()
        assert len(rmse2.errors) == len(rmse2.actual_vals)
        assert rmse2.errors == [9, 9, 4, 9, 4, 4, 1, 1, 4, 9, 16, 1]

    def test_set_mean(self):
        rmse = RMSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        rmse.calc_errors()
        rmse.square_errors()
        rmse.sum_errors()
        rmse.set_mean()
        assert rmse.square_root == 1

        rmse2 = RMSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        rmse2.calc_errors()
        rmse2.square_errors()
        rmse2.sum_errors()
        rmse2.set_mean()
        assert round(rmse2.square_root, 5) == 5.91667

    def test_get_square_root(self):
        rmse = RMSE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        rmse.calc_errors()
        rmse.square_errors()
        rmse.sum_errors()
        rmse.set_mean()
        result = rmse.get_square_root()
        assert result == 1

        rmse2 = RMSE(
            actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
            predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
        )
        rmse2.calc_errors()
        rmse2.square_errors()
        rmse2.sum_errors()
        rmse2.set_mean()
        result2 = rmse2.get_square_root()
        assert round(result2, 5) == 2.43242

