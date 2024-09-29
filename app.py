import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved vectorizer and naive model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
    # Implement your text transformation logic here
    # For example, lowercase, remove punctuation, etc.
    return text.lower()

def predict_spam(text):
    transformed_text = transform_text(text)
    vector_input = tfidf.transform([transformed_text])
    # Get probability scores
    proba = model.predict_proba(vector_input)[0]
    return proba

# Streamlit app
st.title("Email Spam Classifier")
input_sms = st.text_area("Enter message")

if st.button('Predict'):
    proba = predict_spam(input_sms)
    
    # Display probabilities
    st.write(f"Probability of being spam: {proba[1]:.4f}")
    st.write(f"Probability of not being spam: {proba[0]:.4f}")
    
    # Adjust threshold if needed
    threshold = 0.5  # You can adjust this
    result = 1 if proba[1] > threshold else 0
    
    # Display result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    
    # Display feature importance
    feature_names = tfidf.get_feature_names_out()
    feature_importance = model.feature_log_prob_[1] - model.feature_log_prob_[0]
    top_features = sorted(zip(feature_names, feature_importance), key=lambda x: x[1], reverse=True)[:10]
    
    st.subheader("Top spam-indicating features in this message:")
    for word, importance in top_features:
        if word in input_sms.lower():
            st.write(f"{word}: {importance:.4f}")

# Add some example messages for testing
st.sidebar.header("Test with example messages:")
spam_example = "Congratulations! You've won a free iPhone. Click here to claim your prize!"
ham_example = "Hey, can we meet for coffee tomorrow at 3 PM?"

if st.sidebar.button("Test Spam Example"):
    st.text_area("Example Spam Message", spam_example)
    proba = predict_spam(spam_example)
    st.write(f"Probability of being spam: {proba[1]:.4f}")

if st.sidebar.button("Test Ham Example"):
    st.text_area("Example Ham Message", ham_example)
    proba = predict_spam(ham_example)
    st.write(f"Probability of being spam: {proba[1]:.4f}")