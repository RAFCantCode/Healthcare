import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Processed_Data/cleaned_diabetic_data.csv")

print(df.columns)
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
plt.show()
