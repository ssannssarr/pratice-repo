import math
import random

# Training data: OR gate
data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1),
]

# Random weights
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b = random.uniform(-1, 1)

lr = 0.1

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

for epoch in range(10000):
    total_error = 0

    for inputs, target in data:
        x1, x2 = inputs

        # forward pass
        z = x1 * w1 + x2 * w2 + b
        prediction = sigmoid(z)

        error = target - prediction
        total_error += error ** 2

        # learning
        delta = error * sigmoid_derivative(prediction)

        w1 += lr * delta * x1
        w2 += lr * delta * x2
        b += lr * delta

    if epoch % 1000 == 0:
        print("epoch:", epoch, "error:", total_error)

print("\nTrained results:")
for inputs, target in data:
    x1, x2 = inputs
    prediction = sigmoid(x1 * w1 + x2 * w2 + b)
    print(inputs, "=>", round(prediction, 3), "target:", target)
