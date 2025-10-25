import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Processed_Data/cleaned_diabetic_data.csv")

print(df.columns)
age_readmission_counts = df.groupby(['age_group', 'readmission_status']).size().unstack(fill_value=0)

age_read_proportion = age_readmission_counts.div(age_readmission_counts.sum(axis=1), axis=0)
age_order = [
    '[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', 
    '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'
]

age_readmission_counts.index = pd.Categorical(
    age_read_proportion.index, 
    categories=age_order, 
    ordered=True
)
age_readmission_pro = age_read_proportion.sort_index()
plt.figure(figsize=(10,7))
age_readmission_pro.plot(kind='bar', stacked=False, ax=plt.gca(), 
                         color=['mediumseagreen', 'deepskyblue', 'mediumpurple'])
plt.title('Readmission Status By Age Group Proportions')
plt.xlabel('Age Group')
plt.ylabel('Proportion')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=0, ha='center')
plt.tight_layout()
plt.show()