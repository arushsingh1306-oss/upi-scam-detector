import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Load dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "messages.csv")
df = pd.read_csv(data_path)

print(f"Loaded {len(df)} messages")
print(df['label'].value_counts())

# Split data into features (X) and labels (y)
X = df['message']
y = df['label']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate model
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\nModel and vectorizer saved successfully!")

# Test with a few custom messages
test_messages = [
    "Your KYC will expire today, click here to update immediately",
    "Your OTP is 123456, do not share with anyone",
    "Congratulations you won a lottery of Rs 100000, claim now",
]

test_vec = vectorizer.transform(test_messages)
predictions = model.predict(test_vec)
probabilities = model.predict_proba(test_vec)

print("\n--- Sample Predictions ---")
for msg, pred, prob in zip(test_messages, predictions, probabilities):
    confidence = max(prob) * 100
    print(f"Message: {msg}")
    print(f"Prediction: {pred} (Confidence: {confidence:.1f}%)\n")