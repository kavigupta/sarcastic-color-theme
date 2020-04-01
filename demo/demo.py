
import os

import numpy as np
import matplotlib.pyplot as plt

from sarcastic_color_scheme import sarcastic

def test_graph():
    for omega in range(5):
        xs = np.linspace(0, 2 * np.pi / 5, 10)
        plt.plot(xs, np.sin(xs * omega), label=str(omega))
    plt.xlabel("This is the x axis")
    plt.ylabel("This is the y axis")
    plt.title("This is the title")
    plt.legend()

this_folder = os.path.dirname(os.path.abspath(__file__))

with sarcastic:
    for idx in range(3):
        test_graph()
        plt.savefig(os.path.join(this_folder, "sarcastic_{}.png".format(idx)))
        plt.clf()

test_graph()
plt.savefig(os.path.join(this_folder, "back_to_normal.png"))
plt.clf()
