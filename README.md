# Materials Behavior Analyzer

A machine learning project to predict material failure based on mechanical properties — built at the intersection of Mechatronics Engineering and AI.

## 🎯 Goal
Use real or simulated lab data to train a classifier that predicts whether a material specimen will fail under given load conditions.

## 🛠️ Tech Stack
- Python
- Pandas (data processing)
- Scikit-learn (ML models)
- Streamlit (interactive dashboard)

## 📊 Sample Input Features
- Material type (steel, aluminum, copper)
- Yield strength (MPa)
- Tensile strength (MPa)
- Elongation (%)
- Test temperature (°C)
- Test type (Tensile/Compression)
- Heat treated? (Yes/No)

## 🖥️ Output
- Prediction: **Safe** or **Likely to Fail**
- Confidence score (optional)

## 🚀 How to Run
1. Clone this repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Run the dashboard: `streamlit run app.py`

## 📂 Project Structure
material-failure-predictor/
├── material_data.csv # Training data
├── train_model.py # Model training script
├── app.py # Streamlit web app
├── requirements.txt # Dependencies
├── material_failure_model.pkl # Trained model
├── label_encoders.pkl # Text encoders
└── README.md # This file



## 👤 Developer
Wael Noman  
Mechatronics Engineer & AI Enthusiast  
[LinkedIn](https://www.linkedin.com/in/wail-noman)
