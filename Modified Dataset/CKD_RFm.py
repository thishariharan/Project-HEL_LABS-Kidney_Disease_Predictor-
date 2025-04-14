import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load data
train_df = pd.read_excel("CKD_Training_300.xlsx")
test_df = pd.read_excel("CKD_Testing_96.xlsx")

# Replace problematic characters like "\t?" or "?" with NaN
train_df.replace(r'^\s*\?$', np.nan, regex=True, inplace=True)
test_df.replace(r'^\s*\?$', np.nan, regex=True, inplace=True)

# Optionally: print rows with missing values to see what's happening
print("Train missing:\n", train_df.isnull().sum())
print("Test missing:\n", test_df.isnull().sum())

# Fill missing values — basic example: use median (you can customize this!)
train_df.fillna(train_df.median(numeric_only=True), inplace=True)
test_df.fillna(test_df.median(numeric_only=True), inplace=True)

# Extract X and y
X_train = train_df.drop('ckd_classification', axis=1)
y_train = train_df['ckd_classification']
X_test = test_df.drop('ckd_classification', axis=1)
y_test = test_df['ckd_classification']

# Convert to numeric just in case
X_train = X_train.apply(pd.to_numeric)
X_test = X_test.apply(pd.to_numeric)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
# joblib.dump(model, 'CKD_RF_Model.pkl')
print("Model saved!")
