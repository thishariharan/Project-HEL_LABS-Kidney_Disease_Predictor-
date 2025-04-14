import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load training and testing data
train_df = pd.read_excel("DN_Training_660.xlsx")
test_df = pd.read_excel("DN_Testing_102.xlsx")

# Define feature and target columns
X_train = train_df.drop('dn_classification', axis=1)  # Replace 'target' with actual target column name
y_train = train_df['dn_classification']

X_test = test_df.drop('dn_classification', axis=1)
y_test = test_df['dn_classification']

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
# joblib.dump(model, 'DN_RF_Model.pkl')
print("Model saved successfully!")
