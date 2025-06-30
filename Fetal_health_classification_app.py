import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model and scaler
with open('Fetal_Health_Classification_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('feature_list.pkl', 'rb') as f:
    feature_list = pickle.load(f)

st.title("👶 Fetal Health Prediction App")
st.markdown("Enter the fetal health measurements below:")

# Generate input fields dynamically
user_input = {}
for feature in feature_list:
    user_input[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Preprocess
scaled_input = scaler.transform(input_df)

# Predict
if st.button("Predict"):
    prediction = model.predict(scaled_input)[0]
    labels = {1: "Normal", 2: "Suspect", 3: "Pathological"}
    st.success(f"Predicted Fetal Health Condition: **{labels.get(prediction, 'Unknown')}**")

