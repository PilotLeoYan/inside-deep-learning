import numpy as np

def np_mape(pred_value: float|np.ndarray, true_value: float|np.ndarray) -> float:
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between the true value and the predicted value.

    Args:
        pred_value (float or numpy.ndarray): The predicted value.
        true_value (float or numpy.ndarray): The ground truth value.

    Returns:
        float: MAPE.

    Raises:
        TypeError: If one of true_value or pred_value is a numpy.ndarray but the other is not.
        RuntimeError: If true_value and pred_value are numpy.ndarray and their shapes do not match.

    Examples:
    >>> import numpy as np
    >>> from porcentual_error import np_mape
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
    >>> b = np.full((3, 3), 2.0)
    >>> b[0, 0] = 0
    >>> np_mape(b, a)
    0.1111111111111111
    """
    
    # Check if one is a np.ndarray but the other is not
    if isinstance(true_value, np.ndarray) != isinstance(pred_value, np.ndarray):
        raise TypeError("Both true_value and pred_value must be either np.ndarray or numeric types.")

    # If both are arrays, check shape compatibility and calculate error
    if isinstance(true_value, np.ndarray) and isinstance(pred_value, np.ndarray):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')
        mask_zero = true_value == 0
        error_no_zero = np.abs((true_value[~mask_zero] - pred_value[~mask_zero]) / true_value[~mask_zero])
        error_zero = np.abs(pred_value[mask_zero])
        error = (np.sum(error_no_zero) + np.sum(error_zero)) / true_value.size
        return error.item()

    # If both are numeric, calculate the error
    if true_value == 0:
        return abs(pred_value)
    return (true_value - pred_value) / true_value