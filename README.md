# SMS-Spam-Classifier


This project is dedicated to developing an efficient email classification system capable of identifying spam emails with high accuracy, closely emulating the spam detection mechanisms used by phone systems. The primary objective is to create an automated system that can accurately label incoming emails as either spam or legitimate, similar to filtering unwanted calls or messages.

## Objective

The primary objective of this project is to create an automated spam detection system for emails using machine learning techniques. The system leverages a dataset containing labeled messages categorized as "ham" (legitimate) or "spam."

## Dataset

The SMS Spam Collection dataset comprises 5,574 messages in English, meticulously compiled from various sources on the internet, including the Grumble text Website, NUS SMS Corpus, and SMS Spam Corpus. Each message is labeled as either "ham" or "spam."

## Project Development Flow

1. **Data Cleaning**:
   - Remove unwanted features, handle missing values, and standardize column names.
2. **Exploratory Data Analysis (EDA)**:
   - Visualize data distribution, word counts, and characteristics of ham and spam messages.
3. **Data Pre-processing**:
   - Text preprocessing steps like lowercasing, tokenization, special character removal, stop words, punctuation removal, and stemming using the PorterStemmer from NLTK.
   - Generate word clouds for spam and ham messages and identify the top 30 words used in these messages.
4. **Model Building**:
   - Train various classification algorithms including Naive Bayes, Logistic Regression, SVM, Decision Tree, KNN Classifier, Random Forest Classifier, AdaBoost Classifier, Bagging Classifier, ExtraTrees Classifier, Gradient Boosting Classifier, XG Boost Classifier.
   - Compare model performance based on accuracy and precision, identifying Multinomial Naive Bayes as the best-performing model (with 99% precision).
5. **Developing Interface**:
   - Import necessary libraries and setup Streamlit, NLTK, and relevant modules.
   - Load pre-trained models and vectorizers.
   - Define text processing functions for user input.
   - Configure the Streamlit app's settings and create UI elements for user interaction.
   - Implement prediction logic to classify user-provided messages as spam or ham.
   - Provide information about the app creator in the sidebar.

## Interface

The provided Streamlit app offers a user-friendly interface for predicting whether a given text message is spam or ham. Users can input messages, and the app will utilize a pre-trained model to make predictions. Additionally, it provides guidance on identifying spam messages and offers information about the app developer.

## Instructions for Use

To utilize the SMS Spam Classifier:
1. Clone this repository.
2. Install the necessary dependencies mentioned in the requirements file.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Enter a text message into the provided text area.
5. Click the button to classify the message as spam or ham.

## Developer Information

- **Developer:** Divyang Jha
- **Skills:** Machine Learning, Natural Language Processing, Python, Data Analysis

---

This README provides an overview of the project, its objectives, development flow, interface functionality, and guidance on usage. Users can follow the instructions to run the app and understand the project's structure and goals.
