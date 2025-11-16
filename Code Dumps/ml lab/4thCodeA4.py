import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
china_df = pd.read_csv('china_gdp.csv')
X5 = china_df[['Year']]
y5 = china_df['Value']
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5, test_size=0.2, random_state=42)
poly = PolynomialFeatures(degree=3)
X5_train_poly = poly.fit_transform(X5_train)
X5_test_poly = poly.transform(X5_test)
model_poly = LinearRegression()
model_poly.fit(X5_train_poly, y5_train)
y5_pred = model_poly.predict(X5_test_poly)
print(f'Non-linear Regression R²: {r2_score(y5_test, y5_pred):.4f}')
plt.scatter(y5_test, y5_pred)
plt.xlabel('Actual GDP Value')
plt.ylabel('Predicted GDP Value')
plt.title('Actual vs Predicted China GDP')
plt.show()
