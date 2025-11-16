import pandas as pd
import numpy as np

# Create a dataframe
df = pd.DataFrame({
    'ID': range(1, 31),
    'value': [n if n % 5 != 0 else np.nan for n in range(1, 31)],
    'numbers': [n if n % 4 != 0 else '?' for n in range(1, 31)]
})

# Display first few rows
print(df.head())
