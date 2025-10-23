import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Processed_Data/cleaned_diabetic_data.csv")

group = df.groupby('age_group')['hospital_days'].mean().reset_index()
age_order = [
    '[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', 
    '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'
]

group['age_group'] = pd.Categorical(
    group['age_group'], 
    categories=age_order, 
    ordered=True
)

group_index = group.sort_values('age_group')

plt.figure(figsize=(10,8))
sns.barplot(
    data = group_index,
    x = 'age_group',
    y = 'hospital_days',
    hue = 'age_group',
    palette = 'muted'
)
plt.title('Average Hospital Stay By Age Group')
plt.xlabel('Age Groups')
plt.ylabel('Average Hospital Stay')
plt.tight_layout()
plt.show()