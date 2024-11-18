# Regression Error Metrics
Library that implements MAE, MSE & RMSE evaluation metrics.

### Mean Absolute Error (MAE)

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i |
$$

```python
from mae import MAE

mae2 = MAE(
    actual_vals=[12, 13, 14, 15, 15, 22, 27],
    predicted_vals=[11, 13, 14, 14, 15, 16, 18],
)
mae2.calc_errors()
mae2.set_absolute_vals()
mae2.sum_abs_errors()
result2 = mae2.get_mean()
assert round(result2, 5) == 2.42857
```

### Mean Squared Error (MSE)

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

### ### Mean Squared Error (MSE)

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$