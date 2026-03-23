import pandas as pd

df = pd.read_csv('data/raw/ai_jobs.csv')

# 1. Missing values
print(df.isnull().sum())
df.fillna(method='ffill', inplace=True)

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Convert categorical
df['Industry'] = df['Industry'].astype('category')

# 4. Feature Engineering
df['Risk_Level'] = df['Automation_Probability'].apply(
    lambda x: 'High' if x > 0.7 else 'Medium' if x > 0.4 else 'Low'
)

# Convert to binary target
df['At_Risk'] = df['Risk_Level'].apply(lambda x: 1 if x=='High' else 0)

# Save cleaned data
df.to_csv('data/processed/cleaned.csv', index=False)
