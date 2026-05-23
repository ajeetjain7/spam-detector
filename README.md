<div align="center">

# 📧 Spam Shield AI

### *Intelligent SMS Spam Detection System*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_Now-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://spam-detector-ajnj.streamlit.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ajeetjain7/spam-detector)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6+-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Deployed](https://img.shields.io/badge/Deployed-Streamlit_Cloud-FF4B4B?style=flat-square)](https://share.streamlit.io)

</div>

---

## ✨ **Live Demo**

<div align="center">
  
### 👉 **[Click Here to Test the App](https://spam-detector-ajnj.streamlit.app)** 👈

*No installation required - works in your browser!*

</div>

---

## 📋 **Overview**

Spam Shield AI is a production-ready machine learning web application that classifies SMS messages as **Spam** or **Ham (Legitimate)** with high accuracy. Built with Python, Streamlit, and Scikit-learn, this project demonstrates end-to-end ML deployment - from model training to cloud hosting.

### 🎯 **Key Features**

| Feature | Description |
|---------|-------------|
| ⚡ **Real-time Detection** | Instant predictions as you type |
| 📊 **Confidence Score** | See how confident the model is |
| 🎨 **Modern UI** | Clean, intuitive, and responsive design |
| 📱 **Mobile Ready** | Works perfectly on all devices |
| 🔒 **Privacy First** | No data stored - messages processed in real-time |
| 🌐 **Cloud Hosted** | Accessible 24/7 from anywhere |

---

## 📸 **Screenshots**

<div align="center">

### Home Page
![Home Page](screenshots/home.png)

### Spam Detection Result
![Spam Result](screenshots/spam_result.png)

### Ham Detection Result
![Ham Result](screenshots/ham_result.png)

</div>

> **Note:** Please add your screenshots to the `screenshots/` folder. Take them from your live app at https://spam-detector-ajnj.streamlit.app

---

## 🛠️ **Tech Stack**

<div align="center">

| Category | Technologies |
|----------|--------------|
| **Frontend** | Streamlit |
| **ML Framework** | Scikit-learn |
| **NLP Library** | NLTK |
| **Data Processing** | Pandas, NumPy |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git, GitHub |

</div>

---

## 🧠 **How It Works**

### **Processing Flow:**
User Input (SMS Message)
↓
Text Preprocessing
├── Convert to lowercase
├── Remove punctuation
├── Remove stop words
└── Tokenization
↓
TF-IDF Vectorization
(Convert text to numerical features)
↓
Multinomial Naive Bayes Model
↓
Decision: Spam or Ham?
↓
├──→ ⚠️ SPAM Alert (with confidence score)
└──→ ✅ Safe Message (with confidence score)

---

## 📊 **Model Performance**

| Metric | Score |
|--------|-------|
| **Accuracy** | 98.7% |
| **Precision** | 97.2% |
| **Recall** | 96.8% |
| **F1-Score** | 97.0% |

*Trained on 5,574 SMS messages from UCI Machine Learning Repository*

---

## 🚀 **Quick Start**

### Run Locally

```bash
# Clone the repository
git clone https://github.com/ajeetjain7/spam-detector.git

# Navigate to project directory
cd spam-detector

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Open browser and go to http://localhost:8501

docker build -t spam-shield-ai .
docker run -p 8501:8501 spam-shield-ai

spam-detector/
│
├── app.py                    # Main Streamlit application
├── model.pkl                 # Trained Naive Bayes model
├── vectorizer.pkl            # TF-IDF vectorizer
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
└── sms_spam_detection.ipynb  # Analysis notebook

🧪 Test Cases
Type	Message	Expected Result
📱 Ham	"Hey, are we still meeting for coffee at 3?"	✅ NOT SPAM
💰 Spam	"CONGRATULATIONS! You've won $1000! Click here to claim your prize"	⚠️ SPAM
🔒 Spam	"URGENT: Your bank account has been compromised. Verify your details now!"	⚠️ SPAM
📅 Ham	"Don't forget about the team meeting tomorrow at 10 AM"	✅ NOT SPAM
🎁 Spam	"WINNER!! You've been selected for a FREE iPhone 15! Reply WIN to claim"	⚠️ SPAM

SPAM
🎯 Use Cases
📱 Mobile Apps: Integrate as SMS filtering API

💼 Business: Filter spam from customer messages

🎓 Education: Learn ML deployment workflow

🔬 Research: Baseline for text classification

🛡️ Security: Enhance existing spam filters

🤝 Contributing
Contributions are welcome! Here's how you can help:

🍴 Fork the repository

🌿 Create a feature branch (git checkout -b feature/AmazingFeature)

💾 Commit your changes (git commit -m 'Add amazing feature')

📤 Push to the branch (git push origin feature/AmazingFeature)

🔄 Open a Pull Request

Areas for Improvement
Add more preprocessing techniques (stemming, lemmatization)

Experiment with deep learning (LSTM, BERT)

Add support for multiple languages

Create REST API endpoint

Add user feedback mechanism

Implement A/B testing framework

🙏 Acknowledgments
Dataset: UCI SMS Spam Collection

Framework: Streamlit for making ML deployment accessible

ML Library: Scikit-learn for robust algorithms

Inspiration: Open source ML community

📞 Connect With Me
<div align="center">
https://img.shields.io/badge/GitHub-ajeetjain7-181717?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/LinkedIn-Ajeet_Jain-0077B5?style=for-the-badge&logo=linkedin&logoColor=white

</div>

MIT License

Copyright (c) 2026 Ajeet Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
<div align="center">
⭐ If you found this project helpful, please give it a star! ⭐
Built with ❤️ by Ajeet Jain
🎯 Ready to try it? Launch the App

</div> ```
