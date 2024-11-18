# Regression Error Metrics
Library that implements MAE, MSE & RMSE evaluation metrics.

### Mean Absolute Error (MAE)

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i |
$$

```python
from mae import MAE

mae = MAE(
    actual_vals=[12, 13, 14, 15, 15, 22, 27],
    predicted_vals=[11, 13, 14, 14, 15, 16, 18],
)
mae.calc_errors()
mae.set_absolute_vals()
mae.sum_errors()
result = mae.get_mean()
assert round(result, 5) == 2.42857
```

### Mean Squared Error (MSE)

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

```python
from mse import MSE

mse = MSE(
    actual_vals=[34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24],
    predicted_vals=[37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23],
)
mse.calc_errors()
mse.square_errors()
mse.sum_errors()
result = mse.get_mean()
assert round(result, 5) == 5.91667
```

### Root Mean Square Error (RMSE)

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

