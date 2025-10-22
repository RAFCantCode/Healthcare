import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Processed_Data/cleaned_diabetic_data.csv")

source_readmission_counts = df.groupby(['discharge_type_desc', 'readmission_status']).size().unstack()
source_order = sorted(df['discharge_type_desc'].unique())
source_readmission_counts = source_readmission_counts.reindex(source_order, axis=0)
plt.figure(figsize=(10,7))
source_readmission_counts.plot(kind='bar', stacked=False, ax=plt.gca())
plt.title('Readmission Status By source Category')
plt.xlabel('Admission')
plt.ylabel('Count')
plt.legend(title='Readmission Status', loc='upper right')
plt.xticks(rotation=45, ha='center')
plt.tight_layout()
plt.show()