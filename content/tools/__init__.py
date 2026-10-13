"""Tools and metrics package for Inside Deep Learning."""

from .numpy_metrics import np_mape
from .torch_metrics import torch_mape, torch_smape

__all__ = ["np_mape", "torch_mape", "torch_smape"]
