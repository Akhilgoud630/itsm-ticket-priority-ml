import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

df = pd.read_csv("itsm_data.csv")

# ✅ Use only 4 numeric features
X = df[['Impact', 'Urgency', 'No_of_Reassignments', 'Handle_Time_hrs']]
y = df['Priority']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred)*100, 2), "%")
print(classification_report(y_test, y_pred))

joblib.dump(model, "priority_predictor.pkl")
print("✅ Saved new model trained on only 4 features")
