![Python Version](https://img.shields.io/badge/python-3.14.0-blue)
![PyTorch Version](https://img.shields.io/badge/pytorch-2.9.0+cu126-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue)
![Latest commit](https://img.shields.io/github/last-commit/PilotLeoYan/inside-deep-learning)
![Number of issues](https://img.shields.io/github/issues/PilotLeoYan/inside-deep-learning?color=green)
![Number of PRs](https://img.shields.io/github/issues-pr/PilotLeoYan/inside-deep-learning?color=green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
<picture>
   <source media="(prefers-color-scheme: dark)" srcset="content/figures/idl-logo.png" width="500">
   <img alt="Inside Deep learning logo" src="content/figures/idl-logo.png" width="500">
</picture>
</p>

Inside Deep Learning is a collection of Jupyer notebooks aimed at exploring the vast field of machine learning. Sometimes it is difficult to find implementations of important concepts or ideas, so here we try to implement and explain those ideas using upyter Notebooks and PyTorch.

This repository is not intended for beginners or LMs lovers. Rather, it is a compilation of notes on all possible ML topics, especially DL. 

> [!NOTE]
> [View this repository in your browser](https://pilotleoyan.github.io/inside-deep-learning/)

> [!TIP]
> All notebooks are supported for Colab and Jupyter NBViewer.

## Table of Contents

1. [Linear regression 📈](content/1-linear-regression/linear-regression.md)
    1. 🤖 [Simple linear regression](content/1-linear-regression/1-1-simple-linear-regression.ipynb)
    2. 🤖 [Multivariate linear regression](content/1-linear-regression/1-2-multivariate-linear-regression.ipynb)
    3. 🤖 [Multivariate linear regression](content/1-linear-regression/1-3-multioutput-linear-regression.ipynb)
    4. 🤖 [Weight decay (L2 regularization)](content/1-linear-regression/1-4-weight-decay.ipynb)
2. [Classification 📊](content/2-classification/classification.md)
    1. 🤖 [Multiclass classfication](content/2-classification/2-1-multiclass-classification.ipynb)
    + ➗ [Softmax function and its derivative](content/2-classification/softmax-function-and-its-derivative.ipynb)
3. [Multilayer Perceptron 🧠](content/3-multilayer-perceptron/mlp.md)
    1. 🤖 [Multilayer perceptron (MLP)](content/3-multilayer-perceptron/3-1-mlp.ipynb)
    + ➗ [Gradients and activation functions](content/3-multilayer-perceptron/gradients-and-activation-functions.ipynb)
    + 🔵 [MLP for classification](content/3-multilayer-perceptron/mlp-for-classification.ipynb)
    + 🔵 [MLP like PyTorch](content/3-multilayer-perceptron/mlp-like-pytorch.ipynb)
  
> [!TIP]
> 🤖 Programming ML models.
> ➗ Focus on specific concepts, such as mathematics.
> 🔵 Minor variations on the main topics.

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/PilotLeoYan/inside-deep-learning.git
   ```
2. Create environment: <br>
  Inside Deep Learning is written in `python=3.14.0`. We recommend using Conda to manage dependencies.
   ```
   conda create --name idl -y python=3.14.0
   conda activate idl
   pip install --upgrade pip
   cd inside-deep-learning
   ```
3.
   A. Install dependencies with cuda:
   ```
   pip install -r requirements-cuda.txt
   ```
   B. Install dependencies without cuda:
   ```
   pip install -r requirements.txt
   ```

## Used Hardware

* CPU: AMD Ryzen 7
* GPU: Nvidia Geforce RTX 2070-SUPER (8GB VRAM)
* RAM: 16GB DDR4

## Contributing

If you find this repo useful, please star (★) this repo or cite using the following bibtex entry:

```
@misc{pilotleoyan25idl,
  title={Inside-Deep-learning},
  author={Rivera, Leonardo Fabyan Ortega},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished={\url{https://github.com/PilotLeoYan/inside-deep-learning}},
  year={2025}
}
```

## Star History

<a href="https://www.star-history.com/#PilotLeoYan/inside-deep-learning&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PilotLeoYan/inside-deep-learning&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PilotLeoYan/inside-deep-learning&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PilotLeoYan/inside-deep-learning&type=Date" />
 </picture>
</a>

---

If you would like to contact me you can send me an [email](mailto:leofabyano@gmail.com).