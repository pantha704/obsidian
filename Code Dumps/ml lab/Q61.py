# ================================================================
# Question 1
# SVM Classification - Benign vs Malignant Tumor
# Kernels: Linear, Polynomial, RBF, Sigmoid
# ================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, recall_score, precision_score, f1_score,
    jaccard_score, confusion_matrix, roc_curve, auc
)
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Load and clean dataset
# ---------------------------------------------------------------
# Change filename if needed
df = pd.read_csv("samples_cancer.csv")

# Replace '?' with NaN
df.replace('?', np.nan, inplace=True)

# Drop any rows with missing values (or use fillna if preferred)
df.dropna(inplace=True)

# Convert all numeric columns to float (except ID or target)
for col in df.columns:
    if col not in ['id', 'Class']:
        df[col] = df[col].astype(float)

# ---------------------------------------------------------------
# 2. Prepare features and labels
# ---------------------------------------------------------------
# Assuming last column is the target (Class: 2=benign, 4=malignant)
X = df.iloc[:, 1:-1]   # Skip ID column
y = df.iloc[:, -1]

# Convert target to binary (0 = benign, 1 = malignant)
y = y.map({2: 0, 4: 1})

# ---------------------------------------------------------------
# 3. Split dataset
# ---------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------------------------------------------------------------
# 4. Train SVM models with different kernels
# ---------------------------------------------------------------
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
results = {}

plt.figure(figsize=(7, 5))

for kernel in kernels:
    model = SVC(kernel=kernel, probability=True, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluation metrics
    acc = accuracy_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    jac = jaccard_score(y_test, y_pred)
    err = 1 - acc
    cm = confusion_matrix(y_test, y_pred)

    results[kernel] = {
        'Accuracy': acc,
        'Recall': rec,
        'Precision': pre,
        'F1-Score': f1,
        'Jaccard': jac,
        'Error Rate': err,
        'Confusion Matrix': cm
    }

    # ROC curve
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{kernel} (AUC={roc_auc:.2f})')

# ---------------------------------------------------------------
# 5. Plot ROC Curve comparison
# ---------------------------------------------------------------
plt.plot([0, 1], [0, 1], 'k--')
plt.title('ROC Curve Comparison of SVM Kernels')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 6. Print results
# ---------------------------------------------------------------
for k, v in results.items():
    print(f"\n=== Kernel: {k.upper()} ===")
    for metric, value in v.items():
        if metric != 'Confusion Matrix':
            print(f"{metric}: {value:.4f}")
        else:
            print(f"{metric}:\n{value}")
