import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv.csv")

# Encode target
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

X = df.drop('species', axis=1)
y = df['species']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define models to test
models = [
    ("Sigmoid + Adam", "logistic", "adam"),
    ("Tanh + SGD", "tanh", "sgd"),
    ("ReLU + Adam", "relu", "adam"),
]

for name, activation, optimizer in models:
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10, 10, 10),
                        activation=activation,
                        solver=optimizer,
                        max_iter=400,
                        learning_rate_init=0.01,
                        random_state=42)

    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"\n=== {name} ===")
    print("Accuracy:", acc)
    print(classification_report(y_test, y_pred))

    # Plot learning curve
    plt.plot(mlp.loss_curve_, label=f"{name}")

plt.title("Loss Curves for Different Activations/Optimizers")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.show()
