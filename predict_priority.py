import joblib
import pandas as pd

# Load model
model = joblib.load("priority_predictor.pkl")

# Example input (match your training columns)
sample = {
    'CI_Cat_database': 0,
    'CI_Cat_network': 1,
    'CI_Cat_server': 0,
    'CI_Cat_storage': 0,
    'CI_Subcat_Email Service': 0,
    'CI_Subcat_File Server': 0,
    'CI_Subcat_Network Switch': 1,
    'CI_Subcat_SQL Server': 0,
    'CI_Subcat_Web Application': 0,
    'Impact': 2,
    'Urgency': 3,
    'Category_request': 0,
    'Status_closed': 1,
    'Status_in-progress': 0,
    'No_of_Reassignments': 5,
    'Handle_Time_hrs': 120,
    'Closure_Code_Other': 0,
    'Closure_Code_Pending': 0
}

# Convert to DataFrame
df = pd.DataFrame([sample])

# Predict
prediction = model.predict(df)
print("🔮 Predicted Priority Level:", int(prediction[0]))
