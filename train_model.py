import pandas as pd
import re
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

data = pd.read_csv("data/emails.csv")

print("Dataset loaded successfully!")
print(data.head())
print("\nDataset size:", len(data))


# ---------------------------------------
# 2. Clean Dataset
# ---------------------------------------

data = data.dropna(subset=["text", "label"])

data["text"] = data["text"].astype(str)
data["label"] = data["label"].str.lower().str.strip()


# ---------------------------------------
# 3. Feature Extraction
# ---------------------------------------

def extract_features(text):
    text = str(text)

    # Number of URLs
    url_count = len(
        re.findall(
            r"https?://\S+|www\.\S+",
            text
        )
    )

    # Number of suspicious keywords
    suspicious_words = [
        "urgent",
        "verify",
        "verification",
        "password",
        "account",
        "suspended",
        "click",
        "winner",
        "prize",
        "free",
        "confirm",
        "bank",
        "login",
        "security"
    ]

    keyword_count = sum(
        text.lower().count(word)
        for word in suspicious_words
    )

    # Number of exclamation marks
    exclamation_count = text.count("!")

    # Number of HTTP links
    http_count = len(
        re.findall(r"http://", text.lower())
    )

    # Email length
    email_length = len(text)

    return [
        url_count,
        keyword_count,
        exclamation_count,
        http_count,
        email_length
    ]


# Create numerical features

feature_columns = [
    "url_count",
    "keyword_count",
    "exclamation_count",
    "http_count",
    "email_length"
]

data[feature_columns] = data["text"].apply(
    lambda x: pd.Series(extract_features(x))
)


print("\nExtracted Features:")
print(data[feature_columns].head())


# ---------------------------------------
# 4. Convert Text into TF-IDF Features
# ---------------------------------------

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X_text = vectorizer.fit_transform(data["text"])


# ---------------------------------------
# 5. Combine Text + Numerical Features
# ---------------------------------------

from scipy.sparse import hstack
from scipy.sparse import csr_matrix

X_numeric = csr_matrix(
    data[feature_columns].values
)

X = hstack([
    X_text,
    X_numeric
])

y = data["label"]


# ---------------------------------------
# 6. Split Dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# ---------------------------------------
# 7. Train Machine Learning Model
# ---------------------------------------

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

print("\nModel training completed!")


# ---------------------------------------
# 8. Make Predictions
# ---------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------
# 9. Accuracy
# ---------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# ---------------------------------------
# 10. Classification Report
# ---------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ---------------------------------------
# 11. Confusion Matrix
# ---------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["safe", "phishing"]
)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Safe", "Phishing"],
    yticklabels=["Safe", "Phishing"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Phishing Email Detection - Confusion Matrix")

plt.tight_layout()

plt.show()


# ---------------------------------------
# 12. Save Model
# ---------------------------------------

os.makedirs(
    "model",
    exist_ok=True
)

joblib.dump(
    model,
    "model/phishing_model.pkl"
)

joblib.dump(
    vectorizer,
    "model/tfidf_vectorizer.pkl"
)

print("\nModel saved successfully!")