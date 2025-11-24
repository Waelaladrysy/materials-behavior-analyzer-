import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib 

#1. Download data
df = pd.read_csv("material_data.csv")  

#2. Convert text columns to numbers
label_encoders={}

le_material = LabelEncoder()
df['Material'] = le_material.fit_transform(df['Material'])
label_encoders['Material']= le_material

le_test = LabelEncoder()
df['Test_Type']= le_test.fit_transform(df['Test_Type'])
label_encoders['Test_Type']= le_test

#3. Identify input and output
X = df[[
    'Material',
    'Yield_Strength_MPa',
    'Tensile_Strength_MPa',
    'Elongation_%',
    'Temperature_C',
    'Test_Type',
    'Heat_Treated'
]]

y = df['Will_Fail']


#4. Training the Model
model = RandomForestClassifier(n_estimators=100, random_state =42 )
model.fit(X,y) 


#5. Save Form and Text Converters
joblib.dump(model, "material_failure_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")


print('The model has been trained and saved ') 






