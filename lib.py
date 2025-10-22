import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Processed_Data/cleaned_diabetic_data.csv")
# Readmission Status bar graph
readmission_counts = df['readmission_status'].value_counts()
readmission_counts_sorted = readmission_counts.sort_values(ascending=False)

plt.figure(figsize=(8,6))
plt.bar(readmission_counts_sorted.index, readmission_counts_sorted.values, color=['seagreen', 'royalblue', 'violet'])
plt.title('Distribution Of Readmission Status')
plt.xlabel('Readmission Status')
plt.ylabel('Count')

for i, count in enumerate(readmission_counts_sorted.values):
    plt.text(i, count+500, str(count), ha='center')
plt.tight_layout()
plt.savefig('Figures/readmission_status.png')
plt.close()

# Age Group Bar graph
plt.figure(figsize=(15, 10))
age_group = df['age_group'].value_counts()
age_group_sorted = age_group.sort_index(ascending=True)

plt.bar(age_group_sorted.index, age_group_sorted.values, color = 'crimson')
plt.title('Patient Distribution By Age Group')
plt.xlabel('Age Groups')
plt.ylabel('Count')
for i, count in enumerate(age_group_sorted.values):
    plt.text(i, count+500, str(count), ha='center')
plt.tight_layout()
plt.savefig('Figures/age_group.png')
plt.close()

# Readmission status by age group stacked bar graph
age_readmission_counts = df.groupby(['age_group', 'readmission_status']).size().unstack()
age_order = sorted(df['age_group'].unique())
age_readmission_counts = age_readmission_counts.reindex(age_order, axis=0)
plt.figure(figsize=(10,7))
age_readmission_counts.plot(kind='bar', stacked=False, ax=plt.gca())
plt.title('Readmission Status By Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=45, ha='center')
plt.tight_layout()
plt.savefig('Figures/age_groupreadmission_status.png')
plt.close()

# Readmission status by gender status bar graph
read_sex_counts = df.groupby(['sex_identity', 'readmission_status']).size().unstack()
sex_order = sorted(df['sex_identity'].unique())
read_sex_counts = read_sex_counts.reindex(sex_order, axis=0)
plt.figure(figsize=(10,7))
read_sex_counts.plot(kind='bar', stacked=False, ax=plt.gca(), color=['firebrick', 'forestgreen', 'royalblue'])
plt.title('Readmission Status By Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=0, ha='center')
plt.tight_layout()
plt.savefig('Figures/gender_readmission_status.png')
plt.close()

# Readmission status by Ethnic Group
read_ethnic_counts = df.groupby(['ethnic_group', 'readmission_status']).size().unstack()
ethnic_order = sorted(df['ethnic_group'].unique())
read_ethnic_counts = read_ethnic_counts.reindex(ethnic_order, axis=0)
plt.figure(figsize=(10,7))
read_ethnic_counts.plot(kind='bar', stacked=False, ax=plt.gca(), color=['orange', 'orangered', 'crimson'])
plt.title('Readmission Status By Ethnicity')
plt.xlabel('Ethnicity')
plt.ylabel('Count')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=0, ha='center')
plt.tight_layout()
plt.savefig('Figures/ethnicity_readmission_status.png')
plt.close()

# Readmission status by Hospital Stay days box plot
plt.figure(figsize=(8,6))
sns.boxplot(x='readmission_status', y='hospital_days', data=df,
            order=['<30', '>30', 'NO'],
            hue='readmission_status',
            legend=False,
            palette='Set2')
plt.title('Distribution of Hospital Stay Days by Readmission Status')
plt.xlabel('Readmission Status')
plt.ylabel('Hospital Stay Duration')
plt.tight_layout()
plt.savefig('Figures/staydays_readmission_status.png')
plt.close()

# Readmission status by Lab Test Count Box Plot
plt.figure(figsize=(8,6))
sns.boxplot(x='readmission_status', y='lab_test_count', data=df,
            order=['<30', '>30', 'NO'],
            hue='readmission_status',
            legend=False,
            palette='Set3')
plt.title('Number of Lab Tests by Readmission Status')
plt.xlabel('Readmission Status')
plt.ylabel('Number of Lab Tests')
plt.tight_layout()
plt.savefig('Figures/labtest_readmission_status.png')
plt.close()