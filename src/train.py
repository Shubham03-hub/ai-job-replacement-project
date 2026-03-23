import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import os

# Load cleaned data
df = pd.read_csv('data/processed/cleaned.csv')

print("Columns in dataset:")
print(df.columns)

# Features
X = df[['automation_risk_percent',
        'ai_replacement_score',
        'skill_gap_index',
        'salary_before_usd',
        'remote_feasibility_score',
        'ai_adoption_level',
        'reskilling_urgency_score',
        'ai_disruption_intensity']]

# Target
y = df['Risk_Level']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

# Save model
os.makedirs('models', exist_ok=True)
pickle.dump(model, open('models/model.pkl','wb'))

print("Model trained and saved successfully")