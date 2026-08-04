"""
Code to generate the example linear regression approximation
for 'inside-deep-learning/content/1-linear-regression/linear-regression.md'
"""

import numpy as np
import matplotlib.pyplot as plt


def make_plot() -> None:
    np.random.seed(10)

    x1 = np.random.uniform(0, 10, 10)
    x2 = np.random.uniform(0, 10, 10)

    y = 5 + 3 * x1 + 3 * x2 + np.random.normal(0, 5, len(x1))

    X = np.column_stack((np.ones(len(x1)), x1, x2))

    b0, b1, b2 = np.linalg.lstsq(X, y, rcond=None)[0]
    y_pred = b0 + b1 * x1 + b2 * x2

    x1_grid = np.linspace(x1.min(), x1.max(), 20)
    x2_grid = np.linspace(x2.min(), x2.max(), 20)

    X1_grid, X2_grid = np.meshgrid(x1_grid, x2_grid)

    Y_grid = b0 + b1 * X1_grid + b2 * X2_grid

    fig = plt.figure(figsize=(10, 8), facecolor="none")
    ax = fig.add_subplot(111, projection="3d", facecolor="none")

    ax.scatter(
        x1,
        x2,
        y,
        s=60,
        label="Observed data"
    )

    ax.plot_surface(
        X1_grid,
        X2_grid,
        Y_grid,
        alpha=0.35,
        edgecolor="gray",
        linewidth=0.5
    )

    for i in range(len(x1)):
        ax.plot(
            [x1[i], x1[i]],
            [x2[i], x2[i]],
            [y[i], y_pred[i]],
            linestyle=":",
            linewidth=1.5
        )

        ax.scatter(
            x1[i],
            x2[i],
            y_pred[i],
            s=25
        )

    ax.set_xlabel(
        "Independent variable X1",
        bbox=dict(facecolor="white", edgecolor="none", pad=3)
    )

    ax.set_ylabel(
        "Independent variable X2",
        bbox=dict(facecolor="white", edgecolor="none", pad=3)
    )

    ax.set_zlabel(
        "Dependent variable Y",
        bbox=dict(facecolor="white", edgecolor="none", pad=3)
    )

    ax.set_title(
        "Linear Regression: Approximating Data with a Plane",
        bbox=dict(facecolor="white", edgecolor="none", pad=3)
    )

    ax.legend()

    plt.tight_layout()

    plt.savefig(
        "linear-approx.png",
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.4,
    )


if __name__ == '__main__':
    make_plot()