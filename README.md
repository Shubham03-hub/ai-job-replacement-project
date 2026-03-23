# AI Job Replacement Risk Prediction System

## Project Overview
This project focuses on analyzing and predicting the risk of job replacement due to Artificial Intelligence and automation. The system uses data analysis, machine learning, and visualization tools to understand which jobs are at higher risk and why. The project also includes a dashboard and a prediction web application.

The goal of this project is to demonstrate an end-to-end data analytics and data science workflow, starting from raw data and ending with a deployed prediction application.

---

## Problem Statement
With the rapid growth of Artificial Intelligence and automation technologies, many jobs are changing or becoming automated. Companies, governments, and individuals need data-driven insights to understand job risk levels and plan reskilling and workforce strategies.

This project analyzes job-related factors such as salary, automation risk, AI adoption, skill gap, and remote feasibility to predict whether a job is at Low, Medium, or High risk of replacement.

---

## Tools and Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Power BI
- Streamlit
- GitHub

---

## Project Workflow
The project was completed in the following steps:

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Machine Learning Model Training
6. Model Evaluation
7. Saving Trained Model
8. Power BI Dashboard Creation
9. Streamlit Web Application
10. Project Documentation and GitHub Upload

---

## Machine Learning Model
A Random Forest Classifier was used to predict the job risk level.

### Features Used for Prediction:
- automation_risk_percent
- ai_replacement_score
- skill_gap_index
- salary_before_usd
- remote_feasibility_score
- ai_adoption_level
- reskilling_urgency_score
- ai_disruption_intensity

### Target Variable:
- Risk_Level (Low, Medium, High)

The model was trained using a train-test split and evaluated using classification metrics.

---

## Power BI Dashboard
A dashboard was created in Power BI to visualize job risk insights. The dashboard includes:
- Risk Level Distribution
- Industry vs Risk Level
- Country vs Risk Level
- Salary vs Risk Level
- AI Replacement Score vs Risk
- Automation Risk by Industry
- Remote Feasibility Analysis
- Reskilling Urgency Analysis

This dashboard helps understand job automation trends visually.

---

## Streamlit Web Application
A Streamlit web application was built to allow users to input job-related parameters and predict the risk level of job replacement.

The user inputs:
- Automation Risk Percent
- AI Replacement Score
- Skill Gap Index
- Salary
- Remote Feasibility Score
- AI Adoption Level
- Reskilling Urgency Score
- AI Disruption Intensity

The application then predicts whether the job risk is Low, Medium, or High.

---

## Project Structure
ai-job-replacement-project/
│
├── data/
│ ├── raw/
│ └── processed/
│ └── cleaned.csv
│
├── notebooks/
│ ├── eda.ipynb
│ └── ml_model.ipynb
│
├── src/
│ └── train.py
│
├── models/
│ └── model.pkl
│
├── app/
│ └── app.py
│
├── dashboard/
│ └── powerbi.pbix
│
└── README.md


---

## Key Insights from Analysis
- Jobs with higher automation risk percentage are more likely to fall into the high-risk category.
- Jobs with lower remote feasibility and higher skill gaps are more vulnerable to AI replacement.
- Higher AI adoption industries show greater job disruption intensity.
- Reskilling urgency is strongly related to job risk levels.

---

## Conclusion
This project demonstrates a complete data analytics and machine learning workflow. It shows how data can be used to analyze job automation trends and predict job risk levels. The combination of data analysis, machine learning, dashboard visualization, and a web application makes this an end-to-end data science project.

---

## Future Improvements
- Add more data features such as education level and experience
- Try different machine learning models
- Deploy the Streamlit app publicly
- Add SQL database integration
- Build a more interactive dashboard

---

## Author: Shubham Panchal 
Project: AI Job Replacement Risk Prediction System