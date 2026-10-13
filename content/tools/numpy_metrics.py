import numpy as np


def np_mape(
    pred_value: float | int | np.ndarray,
    true_value: float | int | np.ndarray,
) -> float:
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between the true value and the predicted value.

    Args:
        pred_value (float, int, or numpy.ndarray): The predicted value.
        true_value (float, int, or numpy.ndarray): The ground truth value.

    Returns:
        float: MAPE.

    Raises:
        TypeError: If one of true_value or pred_value is a numpy.ndarray but the other is not.
        RuntimeError: If true_value and pred_value are numpy.ndarray and their shapes do not match.

    Examples:
    >>> from numpy_metrics import np_mape
    >>> a = np.full((3, 3), 2.0)
    >>> np_mape(a, a)
    0.0
    >>> np_mape(a * 0, a)
    1.0
    >>> np_mape(-a, a)
    2.0
    >>> np_mape(a, a * 0)
    2.0
    >>> np_mape(-a, a * 0)
    2.0
    >>> np_mape(a * 0, a * 0)
    0.0
    >>> np_mape(-a * 100, a * 100)
    2.0
    """
    # Check if one is a np.ndarray but the other is not
    if isinstance(true_value, np.ndarray) != isinstance(pred_value, np.ndarray):
        raise TypeError("Both true_value and pred_value must be either np.ndarray or numeric types.")

    # If both are arrays, check shape compatibility and calculate error
    if isinstance(true_value, np.ndarray):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')

        mask_zero = true_value == 0
        error_no_zero = np.abs((true_value[~mask_zero] - pred_value[~mask_zero]) / true_value[~mask_zero])
        error_zero = np.abs(pred_value[mask_zero])
        error = (np.sum(error_no_zero) + np.sum(error_zero)) / true_value.size
        return float(error.item())

    # If both are numeric, calculate the error
    if true_value == 0:
        return float(abs(pred_value))
    return float(abs((true_value - pred_value) / true_value))


def np_smape(
    pred_value: float | int | np.ndarray,
    true_value: float | int | np.ndarray,
    eps: float = 1e-16,
) -> float:
    """
    Calculate Symmetric Mean Absolute Percentage Error (SMAPE) between the true value and the predicted value.

    $$
    \text{SMAPE} = \frac{1}{n} \sum_{i=1}^{n}
    \frac{\left| \hat{y}_{i} - y_{i} \right|}{
    \frac{| y_{i} | + | \hat{y}_{i} |}{2}
    + \epsilon}
    $$

    Args:
        pred_value (float, int, or numpy.ndarray): The predicted value.
        true_value (float, int, or numpy.ndarray): The ground truth value.
        eps (float): Epsilon value.

    Returns:
        float: SMAPE.

    Raises:
        TypeError: If one of true_value or pred_value is a numpy.ndarray but the other is not.
        RuntimeError: If true_value and pred_value are numpy.ndarrays and their shapes do not match.
    """
    if isinstance(true_value, np.ndarray) != isinstance(pred_value, np.ndarray):
        raise TypeError("Both true_value and pred_value must be either np.ndarray or numeric types.")

    if isinstance(true_value, np.ndarray):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')

        numerator = np.abs(pred_value - true_value)
        denominator = (np.abs(true_value) + np.abs(pred_value)) / 2 + eps
        error = numerator / denominator
        return float(np.mean(error).item())

    numerator = abs(pred_value - true_value)
    denominator = (abs(true_value) + abs(pred_value)) / 2 + eps
    return float(numerator / denominator)
