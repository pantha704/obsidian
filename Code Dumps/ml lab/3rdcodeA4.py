import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV

salary_df = pd.read_csv('salary_data.csv')

X4 = salary_df['YearsExperience'].values
y4 = salary_df['Salary'].values

# Normalize
X4 = (X4 - np.mean(X4)) / np.std(X4)
X4 = X4.reshape(-1, 1)

# Gradient Descent Parameters
alpha = 0.01  # Learning rate
epochs = 1000
m = len(y4)
theta = np.zeros(2)

X_b = np.c_[np.ones((m, 1)), X4]

for epoch in range(epochs):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y4)
    theta -= alpha * gradients
    if epoch % 100 == 0:
        plt.scatter(X4, y4)
        plt.plot(X4, X_b.dot(theta), color='red')
        plt.title(f'Epoch {epoch}')
        plt.show()

y4_pred = X_b.dot(theta)
print(f'Gradient Descent R²: {r2_score(y4, y4_pred):.4f}')
plt.scatter(y4, y4_pred)
plt.xlabel('Actual Salary')
plt.ylabel('Predicted Salary')
plt.title('Actual vs Predicted Salary')
plt.show()
