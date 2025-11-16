# ================================================================
# Question 2
# SVM, Naive Bayes, Decision Tree, and KNN on Diabetes dataset
# Compare Accuracy, Recall, Precision, F1-score
# Show Confusion Matrix (Heatmap) and ROC Curve
# ================================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, recall_score, precision_score, f1_score,
    confusion_matrix, roc_curve, auc
)

# ---------------------------------------------------------------
# 1. Load dataset (from local folder)
# ---------------------------------------------------------------
# Try both possible filenames
if os.path.exists('pima-indians-diabetes.data.csv'):
    filename = 'pima-indians-diabetes.data.csv'
elif os.path.exists('pima-indians-diabetes.csv'):
    filename = 'pima-indians-diabetes.csv'
else:
    raise FileNotFoundError(
        "⚠️ Dataset not found!\n"
        "Please make sure the file is in the SAME folder as this script.\n"
        "Expected file: 'pima-indians-diabetes.data.csv' or 'pima-indians-diabetes.csv'"
    )

df = pd.read_csv(filename, header=None)
df.columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
]

# ---------------------------------------------------------------
# 2. Clean the data (replace 0s with median values)
# ---------------------------------------------------------------
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for c in cols_with_zeros:
    df[c] = df[c].replace(0, np.nan)
    df[c] = df[c].fillna(df[c].median())  # ✅ no warning version

# ---------------------------------------------------------------
# 3. Prepare data for training
# ---------------------------------------------------------------
X = df.drop(columns=['Outcome'])
y = df['Outcome']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42, stratify=y
)

# ---------------------------------------------------------------
# 4. Define models
# ---------------------------------------------------------------
models = {
    'SVM (RBF)': SVC(kernel='rbf', probability=True, random_state=0),
    'Naive Bayes': GaussianNB(),
    'Decision Tree': DecisionTreeClassifier(random_state=0),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# ---------------------------------------------------------------
# 5. Train, Predict, and Evaluate
# ---------------------------------------------------------------
results = {}

plt.figure(figsize=(8, 6))
for name, clf in models.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Probability scores for ROC
    if hasattr(clf, "predict_proba"):
        y_prob = clf.predict_proba(X_test)[:, 1]
    else:
        y_prob = clf.decision_function(X_test)
        y_prob = (y_prob - y_prob.min()) / (y_prob.max() - y_prob.min())

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    results[name] = {
        'accuracy': acc,
        'recall': rec,
        'precision': prec,
        'f1': f1,
        'confusion_matrix': cm
    }

    # ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=2, label=f'{name} (AUC = {roc_auc:.3f})')

# ---------------------------------------------------------------
# 6. ROC Curve Plot
# ---------------------------------------------------------------
plt.plot([0, 1], [0, 1], 'k--')
plt.title('ROC Curve Comparison (Diabetes Prediction)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 7. Print Metrics and Confusion Matrices
# ---------------------------------------------------------------
for name, r in results.items():
    print(f"\n=== {name} ===")
    print(f"Accuracy : {r['accuracy']:.4f}")
    print(f"Recall   : {r['recall']:.4f}")
    print(f"Precision: {r['precision']:.4f}")
    print(f"F1-Score : {r['f1']:.4f}")

    plt.figure(figsize=(4, 3))
    sns.heatmap(r['confusion_matrix'], annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
