import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa


def create_plot(x_values, y_values, title, x_label, y_label):
    
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig


def save_plot(fig, out_file):
    
    try:
        fig.savefig(out_file, bbox_inches="tight")
    finally:
        plt.close(fig)
