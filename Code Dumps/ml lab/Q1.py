# Logistic Regression - Cancer Classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_curve, auc, accuracy_score
)
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("samples_cancer.csv")

# Check column names
print("Columns in dataset:", df.columns.tolist())

# Encode target (Class: 2 = benign, 4 = malignant)
# Convert to binary (0 = benign, 1 = malignant)
df['Class'] = df['Class'].map({2: 0, 4: 1})

# Handle missing values (if any 'BareNuc' are '?')
df = df.replace('?', pd.NA)
df = df.dropna()
df['BareNuc'] = df['BareNuc'].astype(int)

# Features and target
X = df.drop(['ID', 'Class'], axis=1)
y = df['Class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train logistic regression
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Metrics
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1], [0,1], linestyle='--')
plt.title("ROC Curve - Logistic Regression (Cancer)")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
