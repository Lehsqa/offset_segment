import matplotlib.pyplot as plt


class Plot:
    def __init__(self, figure_1, figure_2):
        self.figure_1 = figure_1
        self.figure_2 = figure_2

    def run(self):
        x1 = [point[0] for point in self.figure_1]
        y1 = [point[1] for point in self.figure_1]

        x2 = [point[0] for point in self.figure_2]
        y2 = [point[1] for point in self.figure_2]

        plt.figure(figsize=(6, 6))

        plt.plot(x1, y1, marker='o', label='Figure 1')
        plt.plot(x2, y2, marker='o', label='Figure 2')

        plt.xlim(min(min(x1), min(x2)) - 1, max(max(x1), max(x2)) + 1)
        plt.ylim(min(min(y1), min(y2)) - 1, max(max(y1), max(y2)) + 1)

        plt.legend()
        plt.grid()
        plt.show()
