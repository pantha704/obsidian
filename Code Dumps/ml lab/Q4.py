# Naive Bayes - Diabetes Prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (no headers in this file)
column_names = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
]
df = pd.read_csv("pima-indians-diabetes.data.csv", header=None, names=column_names)

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)

# Bernoulli Naive Bayes
bnb = BernoulliNB()
bnb.fit(X_train > 0, y_train)
y_pred_bnb = bnb.predict(X_test > 0)

# GaussianNB metrics
print("\n--- Gaussian Naive Bayes ---")
print("Accuracy:", accuracy_score(y_test, y_pred_gnb))
print("F1 Score:", f1_score(y_test, y_pred_gnb))
print(classification_report(y_test, y_pred_gnb))

# BernoulliNB metrics
print("\n--- Bernoulli Naive Bayes ---")
print("Accuracy:", accuracy_score(y_test, y_pred_bnb))
print("F1 Score:", f1_score(y_test, y_pred_bnb))
print(classification_report(y_test, y_pred_bnb))

# Confusion matrices
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.heatmap(confusion_matrix(y_test, y_pred_gnb), annot=True, fmt='d', cmap='Blues')
plt.title("GaussianNB Confusion Matrix")

plt.subplot(1,2,2)
sns.heatmap(confusion_matrix(y_test, y_pred_bnb), annot=True, fmt='d', cmap='Oranges')
plt.title("BernoulliNB Confusion Matrix")
plt.show()
