import streamlit as st 
import pandas as pd
import joblib


# Load the trained model and label encoders 
model = joblib.load("material_failure_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.set_page_config(page_title="Materials Behavior Analyst", page_icon ="🔬")
st.title("🔬 Materials Behavior Analyst")
st.markdown("Enter material properties to predict whether the specimen will **fail** under load.")


# User Input
col1, col2 = st.columns(2)

with col1:
    material = st.selectbox("Material", ["Steel", "Aluminum", "Copper"])
    yield_strength = st.number_input("Yield Strength(MPa)", min_value=0, value=250)
    tensile_strength = st.number_input("Tensile Strength(MPa)", min_value=0, value=400)
    elongation = st.number_input("Elongation (%)", min_value=0, value = 20)


with col2:
    temperature = st.number_input("Temperature (C)", value = 25)
    test_type = st.selectbox("Test_Type", ["Tensile", "Compression"])
    heat_treated = st.radio("Heat Treated?", ["No", "Yes"])
    heat_treated_num  = 1 if heat_treated == "Yes" else 0 


# Encode categorical inputs using the same encoders from training 
material_encoded = label_encoders['Material'].transform([material])[0]
test_type_encoded = label_encoders['Test_Type'].transform([test_type])[0]

# Prediction
if st.button("Analyze Behavior"):
    # Prepare input data for prediction
    input_data = [[
        material_encoded,
        yield_strength,
        tensile_strength,
        elongation,
        temperature,
        test_type_encoded,
        heat_treated_num
    ]]

    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Prediction: The specimen is **likely to fail** under this load!")
    else:
        st.success("✅ Prediction: The specimen is **safe** for use!")


st.markdown("---")
st.caption("Developed by Wail NOMAN | Mechatronics Engineer & AI Enthusiast")