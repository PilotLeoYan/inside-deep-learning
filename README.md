![Python Version](https://img.shields.io/badge/python-3.14.4-blue)
![PyTorch Version](https://img.shields.io/badge/pytorch-2.12.0+cu126-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue)
![Latest commit](https://img.shields.io/github/last-commit/PilotLeoYan/inside-deep-learning)
![Number of issues](https://img.shields.io/github/issues/PilotLeoYan/inside-deep-learning?color=green)
![Number of PRs](https://img.shields.io/github/issues-pr/PilotLeoYan/inside-deep-learning?color=green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
<picture>
   <img alt="Inside Deep learning logo" src="content/figures/main/logo.png" width="500">
</picture>
</p>

**Inside Deep Learning (IDL)**:
Jupyter notebooks exploring machine learning concepts.
This repo provides clear PyTorch implementations and explanations from scratch 
for concepts that are often hard to find.

> [!NOTE]
> This repository uses [workshop-template](https://github.com/jupyter-book/workshop-template) with [MystMD](https://mystmd.org/guide).
>
> [View this repository in your browser](https://pilotleoyan.github.io/inside-deep-learning/)

> [!TIP]
> All notebooks are supported for Colab and Jupyter NBViewer.

## Table of Contents

> [!TIP]
> 🤖 Programming ML models.
> ➗ Focus on a specific concept, such as mathematics proof.
> 🔵 Minor variations on the main topics.

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

## How to Use

> [!IMPORTANT]
> Supported on Linux and Windows. For macOS, check the PyTorch install guide.

1. Clone the repository:
   ```
   git clone https://github.com/PilotLeoYan/inside-deep-learning.git
   ```
2. Create environment: <br>
  Inside Deep Learning is written in `python=3.14`. We recommend using Conda to manage dependencies.
   ```
   conda create --name idl -y python=3.14
   conda activate idl
   pip3 install --upgrade pip
   cd inside-deep-learning
   ```
3.
   A. Install dependencies with cuda:
   ```
   pip3 install -r requirements-cuda.txt
   ```
   B. Install dependencies without cuda:
   ```
   pip3 install -r requirements.txt
   ```

## Used Hardware

* CPU: AMD Ryzen 7
* GPU: Nvidia Geforce RTX 2070-SUPER (8GB VRAM)
* RAM: 16GB DDR4

## Support

If you find this repo useful, please consider starring ★ it on Github:

If you use this work for something, please cite it using the following BibTeX:

```bibtex
@software{ortegarivera2025insidedeeplearning,
  author={Ortega Rivera, Leonardo F.},
  orcid={0009-0004-0497-2808},
  title={Inside Deep learning},
  url={https://github.com/PilotLeoYan/inside-deep-learning},
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
