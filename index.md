---
title: Inside Deep Learning
site:
  hide_outline: true
  hide_toc: false
  hide_title_block: true
---

```{figure} content/figures/main/logo.png
:width: 80%
:align: center
```

```{epigraph}
"What I cannot create, I do not understand."

-- Richard Feynman
```

<h2>Demystifying the Black Box</h2>
<div style="text-align: justify">
In an era dominated by massive foundation models and high-level API calls, 
it is dangerously easy to treat Machine Learning as magic. 
Anyone can <code>pip install</code> a library, pass data to a pre-trained model, and output predictions. 
But when a model diverges, when gradients vanish, or when optimization stalls, 
standard software debugging tools fall short. 
You cannot patch an optimization surface you cannot visualize, 
nor fix an activation function you do not deeply understand.
</br> </br>
<b>Inside Deep Learning</b> 
is a pedagogical exploration designed specifically for engineers and developers who already know how to write clean, 
efficient code but want to bridge the gap between abstract mathematics and practical execution.
</br> </br>
This is not a repository for high-level wrappers or superficial tutorials. 
It is a rigorous journey from <b>first principles</b>. 
Here, we break down core machine learning architectures, derive their mathematical foundations, 
and reconstruct them step-by-step using raw <code>PyTorch</code> and <code>Jupyter Notebooks</code>.
</div>

```{figure} content/figures/main/bluebox.gif
:width: 80%
:align: center
```

<h2>The Landscape: Where We Stand</h2>
<div style="text-align: justify">
To build an intuitive understanding of Deep Learning, 
we must map its position within the broader computational sciences. 
It is not an isolated discipline, but the architectural core of a nested hierarchy:
</div>

```{figure} content/figures/main/venn-diagram.svg
:width: 60%
:align: center
```

<h2>Our Methodology: Code as the Ultimate Proof</h2>
<div style="text-align: justify">
Mathematical proofs in academic papers can often feel detached from engineering realities. 
We believe that clean, readable code is the ultimate validation of theoretical comprehension.
<br><br>
Every topic in this collection is approached via three pillars:
<ol>
  <li><b>The Intuition</b>: Identifying the geometric or statistical problem we aim to solve.</li>
  <li><b>The Mathematics</b>: Deriving the loss functions, gradients, and optimization rules manually.</li>
  <li><b>The Construction</b>: Implementing the mechanics without relying on high-level abstractions like PyTorch's <code>nn.Module</code>, 
  before finally refactoring the code into production-grade patterns.</li>
</ol>
</div>

<div style="text-align: justify">
    <h2>Roadmap of Explorations</h2>
    <h3>Linear Foundations 📈</h3>
    Before tackling non-linear deep networks, 
    we master the bedrock of regression. 
    We explore how continuous targets are modeled, 
    optimized, and mathematically constrained.
</div>

- [Linear Regression Structural Overview](content/1-linear-regression/linear-regression.md)
- 🤖 [Simple Linear Regressio](content/1-linear-regression/1-1-simple-linear-regression.ipynb) - 
Single-variable mapping and Gradient Descent basics.
- 🤖 [Multivariate Linear Regression](content/1-linear-regression/1-2-multivariate-linear-regression.ipynb) -
Scaling features up using matrix operations.
- 🤖 [Multioutput Linear Regression](content/1-linear-regression/1-3-multioutput-linear-regression.ipynb) -
Simultaneously mapping vectors to vectors.
- 🤖 [Weight Decay (L2 Regularization)](content/1-linear-regression/1-4-weight-decay.ipynb)
Constraining model complexity via mathematical penalties.

<div style="text-align: justify">
    <h3>The Mechanics of Classification 📊</h3>
    Moving from continuous outputs to discrete decisions requires transforming 
    arbitrary real numbers into valid probability distributions.
</div>

- [Classification Structural Overview](content/2-classification/classification.md)
- 🤖 [Multiclass Classfication](content/2-classification/2-1-multiclass-classification.ipynb) -
Implementing categorical cross-entropy and tracking decision boundaries.
- ➗ [Softmax function and its Derivative](content/2-classification/softmax-function-and-its-derivative.ipynb) -
A rigorous mathematical breakdown of the engine behind probabilistic classification.

<div style="text-align: justify">
    <h3>Deep Representations: Multilayer Perceptrons 🧠</h3>
    Linear operations fail when data patterns interact non-linearly. 
    Here, we introduce hidden layers and non-linear activations to approximate any continuous function.
</div>

- [MLP Structural Overview](content/3-multilayer-perceptron/mlp.md)
- 🤖 [Multilayer Perceptron (MLP)](content/3-multilayer-perceptron/3-1-mlp.ipynb) -
Building and training our first truly deep architecture.
- ➗ [Gradients and Activation Functions](content/2-classification/softmax-function-and-its-derivative.ipynb) -
Analyzing how non-linearities shape backpropagation.
- 🔵 [MLP for Classification](content/3-multilayer-perceptron/mlp-for-classification.ipynb) -
Combining neural depth with multi-class decision engines.
- 🔵 [MLP like PyTorch](content/3-multilayer-perceptron/mlp-like-pytorch.ipynb) -
Refactoring raw implementations into idiomatic, modular structures.

<div style="text-align: justify">
    <h2>Recommended Theoretical Companions 📚️</h2>
    While this repository provides the implementation backbone, 
    we recommend grounding your studies with these essential academic texts:
</div>

+ Mathematics for Machine Learning (@mml-book) - For underlying linear algebra and calculus.
+ Deep Learning (@Goodfellow) - The gold standard for theoretical deep learning foundations.
+ Dive into Deep Learning (@zhang2023dive) - An excellent interactive breakdown of modern architectures.

## Star History ⭐

```{image} https://api.star-history.com/svg?repos=PilotLeoYan/inside-deep-learning&type=Date
:align: left
```

Give us a star if you like this content in our 
[Github repo](https://github.com/PilotLeoYan/inside-deep-learning).
