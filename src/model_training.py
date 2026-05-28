import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/customer_churn_cleaned.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Target variable
y = df["Churn"]

# Features
X = df.drop(["Churn", "customerID"], axis=1)

print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# One-hot encoding
X = pd.get_dummies(X, drop_first=True)

print("Encoded feature shape:", X.shape)

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))