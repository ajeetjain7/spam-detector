import streamlit as st
import pickle
import os

# Check if pickle files exist
if not os.path.exists('vectorizer.pkl'):
    st.error("vectorizer.pkl not found! Make sure it's in the same folder")
    st.stop()
if not os.path.exists('model.pkl'):
    st.error("model.pkl not found! Make sure it's in the same folder")
    st.stop()

# Load model and vectorizer
@st.cache_resource
def load_artifacts():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

st.title("📧 Spam Message Detector")
st.write("Enter a message to check if it's spam or not")

# Load artifacts
vectorizer, model = load_artifacts()

# User input
message = st.text_area("Message:", height=100)

if st.button("Check Message"):
    if message:
        # Transform and predict
        message_vec = vectorizer.transform([message])
        prediction = model.predict(message_vec)[0]
        probability = model.predict_proba(message_vec)[0]
        
        # Display result
        if prediction == 1:
            st.error(f"⚠️ SPAM detected! (Confidence: {probability[1]*100:.1f}%)")
        else:
            st.success(f"✅ NOT spam (Confidence: {probability[0]*100:.1f}%)")
    else:
        st.warning("Please enter a message")