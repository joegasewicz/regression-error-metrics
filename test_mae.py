from mae import MAE


class TestMAE:

    def test_new(self):
        mae = MAE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        assert isinstance(mae, MAE)

    def test_calc_errors(self):
        mae = MAE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mae.calc_errors()
        assert mae.errors == [-1, 1, -1]

        mae2 = MAE(
            actual_vals=[12, 13, 14, 15, 15, 22, 27],
            predicted_vals=[11, 13, 14, 14, 15, 16, 18],
        )
        mae2.calc_errors()
        assert mae2.errors == [1, 0, 0, 1, 0, 6, 9]

    def test_set_absolute_vals(self):
        mae = MAE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mae.calc_errors()
        mae.set_absolute_vals()
        assert mae.errors == [1, 1, 1]

        mae2 = MAE(
            actual_vals=[12, 13, 14, 15, 15, 22, 27],
            predicted_vals=[11, 13, 14, 14, 15, 16, 18],
        )
        mae2.calc_errors()
        mae2.set_absolute_vals()
        assert mae2.errors == [1, 0, 0, 1, 0, 6, 9]

    def test_sum_abs_errors(self):
        mae = MAE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mae.calc_errors()
        mae.set_absolute_vals()
        mae.sum_abs_errors()
        assert mae.result == 3

        mae2 = MAE(
            actual_vals=[12, 13, 14, 15, 15, 22, 27],
            predicted_vals=[11, 13, 14, 14, 15, 16, 18],
        )
        mae2.calc_errors()
        mae2.set_absolute_vals()
        mae2.sum_abs_errors()
        assert mae2.result == 17

    def test_get_mean(self):
        mae = MAE(actual_vals=[3, 5, 2], predicted_vals=[4, 4, 3])
        mae.calc_errors()
        mae.set_absolute_vals()
        mae.sum_abs_errors()
        result = mae.get_mean()
        assert result == 1

        mae2 = MAE(
            actual_vals=[12, 13, 14, 15, 15, 22, 27],
            predicted_vals=[11, 13, 14, 14, 15, 16, 18],
        )
        mae2.calc_errors()
        mae2.set_absolute_vals()
        mae2.sum_abs_errors()
        result2 = mae2.get_mean()
        assert round(result2, 5) == 2.42857
