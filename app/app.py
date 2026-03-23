import streamlit as st
import pandas as pd
import pickle

st.title("AI Job Risk Prediction")

# Load model
model = pickle.load(open('models/model.pkl', 'rb'))

st.header("Enter Job Details")

automation_risk_percent = st.slider("Automation Risk %", 0.0, 1.0)
ai_replacement_score = st.slider("AI Replacement Score", 0.0, 1.0)
skill_gap_index = st.slider("Skill Gap Index", 0.0, 1.0)
salary_before_usd = st.number_input("Salary Before USD", 1000, 200000)
remote_feasibility_score = st.slider("Remote Feasibility Score", 0.0, 1.0)
ai_adoption_level = st.slider("AI Adoption Level", 0.0, 1.0)
reskilling_urgency_score = st.slider("Reskilling Urgency Score", 0.0, 1.0)
ai_disruption_intensity = st.slider("AI Disruption Intensity", 0.0, 1.0)

if st.button("Predict Risk"):
    input_data = pd.DataFrame([[automation_risk_percent,
                                ai_replacement_score,
                                skill_gap_index,
                                salary_before_usd,
                                remote_feasibility_score,
                                ai_adoption_level,
                                reskilling_urgency_score,
                                ai_disruption_intensity]],
                              columns=['automation_risk_percent',
                                       'ai_replacement_score',
                                       'skill_gap_index',
                                       'salary_before_usd',
                                       'remote_feasibility_score',
                                       'ai_adoption_level',
                                       'reskilling_urgency_score',
                                       'ai_disruption_intensity'])

    prediction = model.predict(input_data)
    st.success(f"Predicted Risk Level: {prediction[0]}")