import torch


def torch_mape(
    pred_value: float | torch.Tensor,
    true_value: float | torch.Tensor,
    eps: float = 1e-16
) -> float:
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between the true value and the predicted value.

    Args:
        pred_value (float or torch.Tensor): The predicted value.
        true_value (float or torch.Tensor): The ground truth value.
        eps (float): Epsilon value.

    Returns:
        float: MAPE.

    Raises:
        TypeError: If one of true_value or pred_value is a torch.Tensor but the other is not.
        RuntimeError: If true_value and pred_value are torch.Tensors and their shapes do not match.

    Examples:
    >>> from torch_metrics import torch_mape
    >>> a = torch.full((3, 3), 2.0)
    >>> torch_mape(a, a)
    0.0
    >>> torch_mape(a * 0, a)
    1.0
    >>> torch_mape(-a, a)
    2.0
    >>> torch_mape(a, a * 0)
    200000000.0
    >>> torch_mape(-a, a * 0)
    200000000.0
    >>> torch_mape(a * 0, a * 0)
    0.0
    >>> torch_mape(-a * 100, a * 100)
    2.0
    """
    # Check if one is a torch.Tensor but the other is not
    if isinstance(true_value, torch.Tensor) != isinstance(pred_value, torch.Tensor):
        raise TypeError("Both true_value and pred_value must be either torch.Tensor or numeric types.")

    # If both are tensors, check shape compatibility and calculate error
    if isinstance(true_value, torch.Tensor):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')

        error = torch.abs((true_value - pred_value) / (true_value + eps))
        return error.mean().item()

    # If both are numeric, calculate the error
    return abs((true_value - pred_value) / (true_value + eps))


def torch_smape(
    pred_value: float | torch.Tensor,
    true_value: float | torch.Tensor,
    eps: float = 1e-16
) -> float:
    """
    Calculate Symmetric Mean Absolute Percentage Error (SMAPE) between the true value and the predicted value.

    $$
    \\text{SMAPE} = \\frac{1}{n} \\sum_{i=1}^{n}
    \\frac{\\left| \\hat{y}_{i} - y_{i} \\right|}{
    \\frac{| y_{i} \\right| + | \\hat{y}_{i} |}{2}
    + \\epsilon}
    $$

    Args:
        pred_value (float or torch.Tensor): The predicted value.
        true_value (float or torch.Tensor): The ground truth value.
        eps (float): Epsilon value.

    Returns:
        float: SMAPE.

    Raises:
        TypeError: If one of true_value or pred_value is a torch.Tensor but the other is not.
        RuntimeError: If true_value and pred_value are torch.Tensors and their shapes do not match.
    """
    # Check if one is a torch.Tensor but the other is not
    if isinstance(true_value, torch.Tensor) != isinstance(pred_value, torch.Tensor):
        raise TypeError("Both true_value and pred_value must be either torch.Tensor or numeric types.")

    # If both are tensors, check shape compatibility and calculate error
    if isinstance(true_value, torch.Tensor):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')

        numerator = torch.abs(pred_value - true_value)
        denominator = (torch.abs(true_value) + torch.abs(pred_value)) / 2 + eps
        error = numerator / denominator
        return error.mean().item()

    # If both are numeric, calculate the error
    numerator = abs(pred_value - true_value)
    denominator = (abs(true_value) + abs(pred_value)) / 2 + eps
    return numerator / denominator
