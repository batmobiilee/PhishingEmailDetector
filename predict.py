import re
import joblib
import pandas as pd

from scipy.sparse import hstack, csr_matrix


# ---------------------------------------
# Load trained model
# ---------------------------------------

model = joblib.load(
    "model/phishing_model.pkl"
)

vectorizer = joblib.load(
    "model/tfidf_vectorizer.pkl"
)


# ---------------------------------------
# Feature extraction
# ---------------------------------------

def extract_features(text):

    text = str(text)

    url_count = len(
        re.findall(
            r"https?://\S+|www\.\S+",
            text
        )
    )

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

    exclamation_count = text.count("!")

    http_count = len(
        re.findall(
            r"http://",
            text.lower()
        )
    )

    email_length = len(text)

    return [
        url_count,
        keyword_count,
        exclamation_count,
        http_count,
        email_length
    ]


# ---------------------------------------
# Get email from user
# ---------------------------------------

print("================================")
print(" PHISHING EMAIL DETECTOR")
print("================================")

email = input(
    "\nEnter the email text:\n"
)


# ---------------------------------------
# Create features
# ---------------------------------------

text_features = vectorizer.transform(
    [email]
)

numeric_features = csr_matrix(
    [extract_features(email)]
)

features = hstack([
    text_features,
    numeric_features
])


# ---------------------------------------
# Prediction
# ---------------------------------------

prediction = model.predict(
    features
)[0]

probability = model.predict_proba(
    features
).max()


# ---------------------------------------
# Display result
# ---------------------------------------

print("\n==============================")

if prediction == "phishing":
    print("RESULT: PHISHING")
else:
    print("RESULT: SAFE")

print(
    f"Confidence: {probability * 100:.2f}%"
)

print("==============================")