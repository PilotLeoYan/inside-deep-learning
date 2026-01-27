import torch


def torch_mape(pred_value: float|torch.Tensor, true_value: float|torch.Tensor) -> float:
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between the true value and the predicted value.

    Args:
        pred_value (float or torch.Tensor): The predicted value.
        true_value (float or torch.Tensor): The ground truth value.

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
    2.0
    >>> torch_mape(-a, a * 0)
    2.0
    >>> torch_mape(a * 0, a * 0)
    0.0
    >>> torch_mape(-a * 100, a * 100)
    """
    
    # Check if one is a torch.Tensor but the other is not
    if isinstance(true_value, torch.Tensor) != isinstance(pred_value, torch.Tensor):
        raise TypeError("Both true_value and pred_value must be either torch.Tensor or numeric types.")

    # If both are tensors, check shape compatibility and calculate error
    if isinstance(true_value, torch.Tensor):
        if true_value.shape != pred_value.shape:
            raise RuntimeError(f'true_value.shape "{true_value.shape}" does not match pred_value.shape "{pred_value.shape}"')
        
        mask_zero = true_value == 0
        error_no_zero = torch.abs((true_value[~mask_zero] - pred_value[~mask_zero]) / true_value[~mask_zero])
        error_zero = torch.abs(pred_value[mask_zero])
        error = (torch.sum(error_no_zero) + torch.sum(error_zero)) / true_value.numel()
        return error.item()

    # If both are numeric, calculate the error
    if true_value == 0:
        return abs(pred_value)
    return abs((true_value - pred_value) / true_value)