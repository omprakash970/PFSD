import matplotlib.pyplot as plt
class Path:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        plt.plot(self.x, self.y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Path Plot')
        plt.grid()
        plt.show()
# Example usage:
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
path = Path(x, y)
path.plot()
