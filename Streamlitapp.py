import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_filename = "logistic_regression_model.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)

# Streamlit app UI
st.title("Heart Disease Prediction App")

# User input fields
def user_input_features():
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=50)
    sex = st.radio("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3], format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"][x])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=400, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "False" if x == 0 else "True")
    restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2], format_func=lambda x: ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"][x])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2], format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
    ca = st.number_input("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
    thal = st.selectbox("Thalassemia Type", options=[0, 1, 2, 3], format_func=lambda x: ["Error", "Fixed Defect", "Normal", "Reversible Defect"][x])
    
    data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal,
    }
    return pd.DataFrame([data])

# Get user input
df_input = user_input_features()

# Predict button
if st.button("Predict Heart Disease"):
    prediction = model.predict(df_input)
    result = "Positive for Heart Disease" if prediction[0] == 1 else "Negative for Heart Disease"
    st.write(f"Prediction: {result}")


