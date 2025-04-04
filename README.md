![Python Version](https://img.shields.io/badge/python-3.13-blue)
![PyTorch Version](https://img.shields.io/badge/pytorch-2.6.0-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue) <br>
![Latest commit](https://img.shields.io/github/last-commit/PilotLeoYan/inside-deep-learning)
![Number of issues](https://img.shields.io/github/issues/PilotLeoYan/inside-deep-learning?color=green)
![Number of PRs](https://img.shields.io/github/issues-pr/PilotLeoYan/inside-deep-learning?color=green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
<picture>
   <source media="(prefers-color-scheme: dark)" srcset="images/inside-deep-learning-logo.png">
   <img alt="Inside Deep learning logo" src="images/inside-deep-learning-logo.png">
</picture>
</p>

This repository is a collection of Jupyer notebooks aimed at exploring the vast field of machine learning. Sometimes it is difficult to find implementations of important concepts or ideas, so here we try to implement and explain those ideas using Markdown and Pytorch. 

This repository is not for beginners, not just for LMs, but for anyone who is curious.

> [!NOTE]
> Some formulas in $\LaTeX$ may not render well on Github.

> [!TIP]
> All notebooks are supported for Colab.

## Table of Contents

1. [Linear regression 📈](1-linear-regression)
    1. [Simple linear regression](1-linear-regression/1-1-simple-linear-regression.ipynb)
    2. [Multivariate linear regression](1-linear-regression/1-2-multivariate-linear-regression.ipynb)
    3. [Weight decay (L2 regularization)](1-linear-regression/1-3-weight-decay.ipynb)
    4. [Interpretability and Generalization](1-linear-regression/1-4-interpretability-generalization.ipynb)
    + [Weight decay and Normal equation](1-linear-regression/weight-decay-and-normal-equation.ipynb)
2. [Classification 📊](2-classification)
    1. [Multiclass classfication](2-classification/2-1-multiclass-classification.ipynb)
    + [Softmax function and its derivative](2-classification/softmax-function-and-its-derivative.ipynb)
3. [Multilayer Perceptron 🧠](3-multilayer-perceptron)
    1. [Multilayer perceptron (MLP)](3-multilayer-perceptron/3-1-mlp.ipynb)
    + [Gradients and activation functions](3-multilayer-perceptron/gradients-and-activation-functions.ipynb)
    + [MLP for classification](3-multilayer-perceptron/mlp-for-classification.ipynb)
    + [MLP like PyTorch](3-multilayer-perceptron/mlp-like-pytorch.ipynb)
  
> [!TIP]
> The items listed are notebooks that build on the previous ones.
> The parts that aren't numbered are for math development.

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/PilotLeoYan/inside-deep-learning.git
   ```
2.
   A. Install dependencies with cuda:
   ```
   pip install -r requirements-cuda.txt
   ```
   B. Install dependencies without cuda:
   ```
   pip install -r requirements.txt
   ```

## Examples

[Interpretability and Generalization](1-linear-regression/1-4-interpretability-generalization.ipynb)
<p align="center">
    <img src="images/ridge-regression-training.gif" width="520"\>
</p>

## Used hardware

* CPU: AMD A6-9500
* GPU: Nvidia Geforce RTX 2070-SUPER (8GB VRAM)
* RAM: 16GB DDR4

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new topics to add, feel free to open an issue. Please follow the [contributing guidelines](CONTRIBUTING.md).
Remember that I am only one person working on this repository.

## Main Bibliography

<a id="1">[1]</a> 
**Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press. [URL](http://www.deeplearningbook.org).

<a id="2">[2]</a> 
**Zhang, A., Lipton, Z. C., Li, M., & Smola, A. J.** (2023). *Dive into Deep Learning*. Cambridge University Press. [URL](https://D2L.ai).

<a id="3">[3]</a> 
**Deisenroth, M. P., Faisal, A. A., & Ong, C. S.** (2020). *Mathematics for Machine Learning*. Cambridge University Press. [URL](https://mml-book.github.io/).

---

If you would like to contact me you can send me an [email](mailto:leofabyano@gmail.com).
