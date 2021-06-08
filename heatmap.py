import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("chess.csv")
white_king = df["White King"].to_list()
black_king = df["Black King"].to_list()


def new_func(piece):
    data = np.array(piece).reshape(8, 8)  # transform to 2D
    data = np.flipud(data)
    ax = sns.heatmap(data, cmap='mako_r', cbar=True, square=True)
    ax.set_yticklabels([8, 7, 6, 5, 4, 3, 2, 1])
    ax.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    plt.show()


new_func(white_king)
new_func(black_king)
