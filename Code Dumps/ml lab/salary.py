import pandas as pd

# Read dataset from URL (after downloading from Kaggle)
df = pd.read_csv("Salary_dataset.csv")

# 1. Dataset info
print("Dataset Info:")
print(df.shape)  # Number of rows and columns

# 2. First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Random subset of 5 rows
print("\nRandom Subset of 5 Rows:")
print(df.sample(5))
