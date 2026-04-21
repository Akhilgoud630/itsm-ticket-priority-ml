from flask import Flask, render_template, request
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("priority_predictor.pkl")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    Impact = int(request.form['Impact'])
    Urgency = int(request.form['Urgency'])
    No_of_Reassignments = int(request.form['No_of_Reassignments'])
    Handle_Time_hrs = float(request.form['Handle_Time_hrs'])

    # Simple input structure (minimal example)
    data = {
        'Impact': [Impact],
        'Urgency': [Urgency],
        'No_of_Reassignments': [No_of_Reassignments],
        'Handle_Time_hrs': [Handle_Time_hrs],
    }

    df = pd.DataFrame(data)

    # Predict
    prediction = model.predict(df)[0]

    return render_template('index.html', prediction_text=f'Predicted Ticket Priority: {int(prediction)}')

if __name__ == '__main__':
    app.run(debug=True)
