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
age_readmission_counts = df.groupby(['age_group', 'readmission_status']).size().unstack(fill_value=0)


age_order = [
    '[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', 
    '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'
]

age_readmission_counts.index = pd.Categorical(
    age_readmission_counts.index, 
    categories=age_order, 
    ordered=True
)
age_readmission_counts = age_readmission_counts.sort_index()
plt.figure(figsize=(10,7))
age_readmission_counts.plot(kind='bar', stacked=False, ax=plt.gca())
plt.title('Readmission Status By Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=0, ha='center')
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

# Gender Proportion
read_sex_counts = df.groupby(['sex_identity', 'readmission_status']).size().unstack()
read_sex_proportions = read_sex_counts.div(read_sex_counts.sum(axis=1), axis=0)
sex_order = sorted(df['sex_identity'].unique())
read_sex_counts = read_sex_proportions.reindex(sex_order, axis=0)
plt.figure(figsize=(10,7))
read_sex_counts.plot(kind='bar', stacked=False, ax=plt.gca(), color=['firebrick', 'forestgreen', 'royalblue'])
plt.title('Readmission Proportions By Gender')
plt.xlabel('Gender')
plt.ylabel('Proportion of Readmission')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=0, ha='center')
plt.tight_layout()
plt.savefig('Figures/gender_proportion_readmission_status.png')
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

# Medication Count Of Patients
medication_count = df['medication_count'].value_counts()
medication_count_sorted = medication_count.sort_values(ascending=False)
medication_count_filtered = medication_count_sorted[medication_count_sorted.index <= 70]
plt.figure(figsize=(8,6))
plt.bar(medication_count_filtered.index, medication_count_filtered.values, color=['green'])
plt.title('Medication Count of Patients')
plt.xlabel('Medication Count')
plt.ylabel('Number Of Patients')
plt.tight_layout()
plt.savefig('Figures/medication_count.png')
plt.close()

# Medication Count By Readmission Status Box Plot
plt.figure(figsize=(8,6))
sns.boxplot(x = 'readmission_status', y = 'medication_count', data = df,
            order = ['<30', '>30', 'NO'],
            hue='readmission_status',
            legend = False,
            palette = 'Set1',
        )
plt.title('Medication Count by Readmission Status')
plt.xlabel('Readmission Status')
plt.ylabel('Medication Count')
plt.tight_layout()
plt.savefig('Figures/medication_count_readmission_status.png')
plt.close()


# Hospital stay Days
days = df['hospital_days'].value_counts()
days_sorted = days.sort_values(ascending=False)

plt.figure(figsize=(12,6))
plt.bar(days_sorted.index, days_sorted.values)
plt.title('Number of Hospital Days')
plt.xlabel('Days stayed in the Hospital')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Figures/hospitaldays.png')
plt.close()


# Average Hospital Days based on Age Groups
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
plt.savefig('Figures/avg_hospitaldays_by_age.png')
plt.close()

# Average Med count by age group

group = df.groupby('age_group')['medication_count'].mean().reset_index()
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
    y = 'medication_count',
    hue = 'age_group',
    palette = 'mako'
)
plt.title('Average Medication Count By Age Group')
plt.xlabel('Age Groups')
plt.ylabel('Average Medications Taken')
plt.tight_layout()
plt.savefig('Figures/avg_medcount_by_age.png')
plt.close()

# Readmission types By Admission Sources
read_adm = df.groupby(['admission_type_desc', 'readmission_status']).size().unstack()
adm_order = ['Emergency', 'Elective', 'Urgent']
read_adm = read_adm.reindex(adm_order, axis=0)
readm_order = ['<30', '>30', 'NO']
read_adm_counts = read_adm.reindex(columns=readm_order, fill_value=0)
plt.figure(figsize=(10,8))
read_adm_counts.plot(kind='bar',stacked=False, ax=plt.gca(), color = ['darkorange', 'indianred', 'blueviolet'])
plt.title("Readmission Counts By Admission Type")
plt.xlabel('Type Of Admission')
plt.ylabel('Counts')
plt.xticks(rotation=0, ha='center')
plt.legend(title='Readmission Status', loc='upper right')
plt.tight_layout()
plt.savefig('Figures/admission_type_readm_status.png')
plt.close()