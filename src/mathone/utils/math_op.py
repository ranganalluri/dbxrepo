import numpy as np

class MathOperations:
    def __init__(self, data):
        self.data = data

    def add(self, value):
        return np.add(self.data, value)

    def subtract(self, value):
        return np.subtract(self.data, value)

    def multiply(self, value):
        return np.multiply(self.data, value)

    def divide(self, value):
        return np.divide(self.data, value) if value != 0 else "Cannot divide by zero"