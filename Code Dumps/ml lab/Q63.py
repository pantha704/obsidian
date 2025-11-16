# ================================================================
# Question 3
# K-Means Clustering for Customer Segmentation
# Using Euclidean and Manhattan distance
# ================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from mpl_toolkits.mplot3d import Axes3D

# ---------------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------------
df = pd.read_csv("Cust_Segmentation.csv")  # 👈 Your dataset name
print("✅ Dataset loaded successfully!\n")
print(df.head())

# ---------------------------------------------------------------
# 2. Select numerical features for clustering
# ---------------------------------------------------------------
# Using columns that exist in your file
X = df[['Age', 'Income', 'DebtIncomeRatio']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------------------------------------------------------
# 3. Find optimal number of clusters (Elbow Method)
# ---------------------------------------------------------------
distortions = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    distortions.append(
        sum(np.min(cdist(X_scaled, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X_scaled.shape[0]
    )

plt.figure(figsize=(6, 4))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Average Distortion')
plt.title('Elbow Method (Euclidean Distance)')
plt.show()

# ---------------------------------------------------------------
# 4. Apply K-Means (choose k based on elbow, example k=4)
# ---------------------------------------------------------------
k = 4
kmeans_euclidean = KMeans(n_clusters=k, random_state=42)
df['Cluster_Euclidean'] = kmeans_euclidean.fit_predict(X_scaled)

# Manhattan distance version
dist_matrix = cdist(X_scaled, kmeans_euclidean.cluster_centers_, metric='cityblock')
df['Cluster_Manhattan'] = np.argmin(dist_matrix, axis=1)

# ---------------------------------------------------------------
# 5. Visualize Clusters (2D)
# ---------------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df['Income'], df['DebtIncomeRatio'],
            c=df['Cluster_Euclidean'], cmap='rainbow')
plt.title('Customer Segments (Euclidean Distance)')
plt.xlabel('Income')
plt.ylabel('DebtIncomeRatio')
plt.show()

# ---------------------------------------------------------------
# 6. Visualize Clusters (3D)
# ---------------------------------------------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Age'], df['Income'], df['DebtIncomeRatio'],
           c=df['Cluster_Euclidean'], cmap='rainbow')
ax.set_xlabel('Age')
ax.set_ylabel('Income')
ax.set_zlabel('DebtIncomeRatio')
ax.set_title('3D View of Customer Segments')
plt.show()

print("\n✅ Clustering complete! Check the 2D and 3D plots.")
