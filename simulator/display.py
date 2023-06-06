import os
import matplotlib.pyplot as plt
import numpy as np

import constants

class Display:
    def __init__(self, terminal, time_constant):
        self.time_constant = time_constant
        if terminal:
            self.render = self.terminal_render
        else:
            _, ax = plt.subplots()
            self.image = ax.imshow(np.eye(constants.CANVAS_SIZE, constants.CANVAS_SIZE)) 
            self.render = self.matplotlib_render

    def matplotlib_render(self, matrix):
        self.image.set_array(matrix)
        plt.draw()
        plt.pause(0.001)

    def terminal_render(self, matrix):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(matrix.shape[0]):
            for c in range(matrix.shape[1]):
                print(2*"\u25A0", end='') if (matrix[r, c]) else  print(2*' ', end='')
            print("")