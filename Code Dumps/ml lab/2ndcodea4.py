import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV

housing_df = pd.read_csv('housing_price_dataset.csv')

X3 = housing_df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                 'Avg. Area Number of Bedrooms', 'Area Population']]
y3 = housing_df['Price']

X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

# Lasso Regression with hyperparameter tuning
lasso = Lasso()
params = {'alpha': [0.01, 0.1, 1, 10, 100]}
grid_lasso = GridSearchCV(lasso, param_grid=params, cv=5)
grid_lasso.fit(X3_train, y3_train)
lasso_pred = grid_lasso.predict(X3_test)

print(f'Lasso Best Alpha: {grid_lasso.best_params_}')
print(f'Lasso R²: {r2_score(y3_test, lasso_pred):.4f}')
plt.scatter(y3_test, lasso_pred)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Lasso: Actual vs Predicted House Price')
plt.show()

ridge = Ridge()
grid_ridge = GridSearchCV(ridge, param_grid=params, cv=5)
grid_ridge.fit(X3_train, y3_train)
ridge_pred = grid_ridge.predict(X3_test)
print(f'Ridge Best Alpha: {grid_ridge.best_params_}')
print(f'Ridge R²: {r2_score(y3_test, ridge_pred):.4f}')
plt.scatter(y3_test, ridge_pred)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Ridge: Actual vs Predicted House Price')
plt.show()
