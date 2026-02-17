# Fake-News-Detector-App
# 📰 Fake News Detection Desktop Application

A Machine Learning based desktop application that detects whether a news article is **Real or Fake** using Natural Language Processing (NLP) techniques.

---

## 🚀 Project Overview

This project uses a supervised Machine Learning model trained on a large Fake and Real News dataset.  
The application analyzes user-input news text and predicts whether it is:

✅ Real News  
❌ Fake News  

The model was trained using TF-IDF vectorization and Logistic Regression, achieving high accuracy on the test dataset.

---

## 🧠 Machine Learning Details

- Dataset: Fake and Real News Dataset (Kaggle)
- Text Preprocessing:
  - Lowercasing
  - Removing punctuation
  - Removing numbers
- Feature Extraction:
  - TF-IDF Vectorizer
- Model Used:
  - Logistic Regression
- Model Accuracy:
  - 99% accuracy on test dataset

---

## 🖥️ Application Features

- Simple and clean user interface
- Desktop application (converted using PyInstaller)
- Instant prediction (Real or Fake)
- Lightweight and fast
- End-to-end ML workflow implementation

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- NumPy
- SciPy
- Joblib
- PyWebView
- HTML
- CSS

---

## 📂 Project Structure

Fake-News-Detector-App/
│
├── app.py  
├── model.pkl  
├── vectorizer.pkl  
├── requirements.txt  
│  
├── templates/  
│   └── index.html  
│  
└── static/  
    └── style.css  

---

## ▶️ How to Run the Project

1️⃣ Install required libraries:

pip install -r requirements.txt

2️⃣ Run the application:

python app.py

The desktop window will open automatically.

---

## 🎯 How It Works

1. User enters news text.
2. Text is cleaned and preprocessed.
3. TF-IDF vectorizer transforms text into numerical features.
4. Trained Logistic Regression model predicts:
   - Real News
   - Fake News

---

## 📌 Future Improvements

- Add confidence score display
- Improve UI design
- Add web deployment
- Integrate real-time fact-checking APIs
- Expand dataset for global news coverage

---

## 👩‍💻 Author

Sakshi Khatale  
Machine Learning Enthusiast

