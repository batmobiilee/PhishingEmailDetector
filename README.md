# Phishing Email Detector Using Machine Learning

A machine learning-based application that detects whether an email is **Phishing** or **Safe** using Python and Scikit-learn. The system analyzes the textual content of emails and extracts additional features such as URLs, suspicious keywords, HTTP links, special characters, and email length.

## 📌 Project Overview

Phishing emails are fraudulent messages designed to trick users into revealing sensitive information such as passwords, banking details, or login credentials.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to automatically classify emails into two categories:

* 🔴 **Phishing**
* 🟢 **Safe**

The model uses **TF-IDF text features** combined with manually extracted email features and trains a **Logistic Regression** classifier.

---

## 🚀 Features

* Train a machine learning model using a labeled email dataset
* Classify emails as **Phishing** or **Safe**
* Extract textual features using **TF-IDF**
* Detect and count URLs
* Detect suspicious keywords
* Count HTTP links
* Count exclamation marks
* Analyze email length
* Calculate model accuracy
* Generate a classification report
* Display a confusion matrix
* Save the trained machine learning model
* Test new emails using a prediction program

---

## 🧠 Machine Learning Workflow

```text
                 Email Dataset
                      │
                      ▼
                Data Cleaning
                      │
                      ▼
              Feature Extraction
             ┌────────┴─────────┐
             │                  │
         TF-IDF             Email Features
         Features           ┌─────────────┐
                            │ URL Count   │
                            │ Keywords    │
                            │ HTTP Count  │
                            │ ! Count     │
                            │ Email Length│
                            └──────┬──────┘
             │                     │
             └─────────┬───────────┘
                       ▼
                 Feature Matrix
                       │
                       ▼
              Logistic Regression
                       │
                       ▼
                 Classification
                ┌──────┴──────┐
                ▼             ▼
             Phishing        Safe
```

---

## 🛠️ Technologies Used

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Programming language     |
| Pandas       | Data processing          |
| NumPy        | Numerical operations     |
| Scikit-learn | Machine learning         |
| SciPy        | Sparse matrix operations |
| Matplotlib   | Data visualization       |
| Seaborn      | Confusion matrix         |
| Joblib       | Saving trained models    |
| VS Code      | Development environment  |
| Git & GitHub | Version control          |

---

## 📁 Project Structure

```text
PhishingEmailDetector/
│
├── data/
│   └── emails.csv
│
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── train_model.py
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The dataset is stored in:

```text
data/emails.csv
```

The CSV file contains two columns:

```text
text,label
```

Example:

```csv
text,label
"URGENT! Your bank account has been suspended. Verify immediately.","phishing"
"Hi John, can you send me the assignment before 5 PM?","safe"
```

The `label` column contains:

```text
phishing
safe
```

> **Note:** The small sample dataset included for testing is intended to demonstrate the project workflow. For meaningful machine-learning evaluation, a larger and diverse dataset should be used.

---

## 🔍 Feature Extraction

### 1. TF-IDF

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert email text into numerical features.

For example:

```text
"verify your account immediately"
```

is converted into a numerical representation that can be processed by the machine-learning model.

### 2. URL Features

The system counts URLs found in an email.

Example:

```text
https://example.com/login
```

### 3. Suspicious Keywords

The system checks for keywords commonly associated with phishing messages, including:

```text
urgent
verify
password
account
suspended
click
winner
prize
confirm
bank
login
security
```

### 4. Other Features

The model also considers:

* Number of URLs
* Number of suspicious keywords
* Number of exclamation marks
* Number of HTTP links
* Email length

---

## 🤖 Machine Learning Model

The project uses **Logistic Regression** for classification.

The dataset is divided into:

```text
Training Data → 80%
Testing Data  → 20%
```

The model learns patterns from the training data and evaluates its performance on previously unseen test data.

---

## 📈 Model Evaluation

The project calculates:

### Accuracy

Measures the percentage of correctly classified emails.

```text
Accuracy =
Correct Predictions / Total Predictions
```

### Classification Report

The classification report provides:

* Precision
* Recall
* F1-score
* Support

### Confusion Matrix

The confusion matrix shows how many emails were correctly and incorrectly classified.

```text
                 Predicted
                 Safe   Phishing

Actual Safe       TN       FP

Actual Phishing  FN       TP
```

Where:

* **TN** = True Negative
* **FP** = False Positive
* **FN** = False Negative
* **TP** = True Positive

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PhishingEmailDetector.git
```

Move into the project:

```bash
cd PhishingEmailDetector
```

Replace `YOUR_USERNAME` with your GitHub username.

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

The program will:

1. Load the dataset
2. Clean the data
3. Extract email features
4. Convert text into TF-IDF features
5. Split the dataset
6. Train the Logistic Regression model
7. Calculate accuracy
8. Display the classification report
9. Display the confusion matrix
10. Save the trained model

The trained models will be saved inside:

```text
model/
```

---

## 🔮 Predict a New Email

After training the model, run:

```bash
python predict.py
```

Enter an email when prompted.

Example:

```text
URGENT! Your bank account has been suspended.
Verify your password immediately by clicking
http://example.com/login
```

The program will display something similar to:

```text
==============================
RESULT: PHISHING
Confidence: 96.20%
==============================
```

For a legitimate email:

```text
Hi John,

The project meeting is scheduled for tomorrow at 10 AM.
Please bring the project report.
```

The result may look like:

```text
==============================
RESULT: SAFE
Confidence: 91.30%
==============================
```

The exact confidence depends on the dataset and trained model.

---

## 📦 Generated Model Files

After running `train_model.py`, the following files are created:

```text
model/
├── phishing_model.pkl
└── tfidf_vectorizer.pkl
```

### phishing_model.pkl

Contains the trained Logistic Regression model.

### tfidf_vectorizer.pkl

Contains the TF-IDF vectorizer used to convert email text into numerical features.

---

## ⚠️ Limitations

This project is intended as an educational machine-learning project and should not be treated as a complete production-grade email security system.

Potential limitations include:

* Dataset size and quality affect model performance.
* New phishing techniques may not be recognized.
* Suspicious words can appear in legitimate emails.
* Legitimate emails can contain URLs.
* Model confidence does not guarantee that an email is actually safe or malicious.
* Accuracy alone is not sufficient for evaluating a phishing detector.

For a production system, additional URL analysis, domain reputation, sender authentication, attachment analysis, and continuously updated threat intelligence would be required.

---

## 🔮 Future Improvements

Possible future improvements include:

* Use a larger real-world dataset
* Add more URL-based features
* Analyze sender information
* Analyze email headers
* Detect suspicious domains
* Analyze attachments
* Add Random Forest and SVM models
* Compare multiple machine-learning algorithms
* Add cross-validation
* Add precision-recall curves
* Build a web interface using Flask or FastAPI
* Add a browser-based email analysis interface
* Deploy the application online
* Add a database for storing analysis results

---

## 🎯 Expected Outcome

The completed system should be able to analyze the textual content and selected structural characteristics of an email and classify it as:

```text
Phishing
```

or:

```text
Safe
```

The system also provides quantitative evaluation through accuracy, precision, recall, F1-score, and a confusion matrix.

---

## 📄 License

This project is intended primarily for educational and academic purposes.
