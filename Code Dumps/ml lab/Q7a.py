import numpy as np

# XOR Input and Output
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Activation function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights randomly
np.random.seed(42)
w0 = np.random.uniform(size=(2, 2))   # input -> hidden
w1 = np.random.uniform(size=(2, 1))   # hidden -> output
b0 = np.random.uniform(size=(1, 2))
b1 = np.random.uniform(size=(1, 1))

# Training parameters
lr = 0.1
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_input = np.dot(X, w0) + b0
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, w1) + b1
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = d_output.dot(w1.T) * sigmoid_derivative(hidden_output)

    # Weight updates
    w1 += hidden_output.T.dot(d_output) * lr
    w0 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_output, axis=0, keepdims=True) * lr
    b0 += np.sum(d_hidden, axis=0, keepdims=True) * lr

# Test
print("Predicted Output:")
print(np.round(final_output))
