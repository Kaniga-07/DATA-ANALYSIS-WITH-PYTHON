import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame creation (you should replace this with loading your actual dataset)
data = {
    'chol': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    'fbs': [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    'restecg': [0, 1, 0, 2, 0, 1, 0, 1, 0, 2],
    'thalach': [150, 160, 170, 180, 120, 130, 140, 150, 160, 170],
    'exang': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'oldpeak': [1.0, 1.5, 2.0, 0.5, 1.2, 1.3, 0.8, 1.0, 1.4, 0.7],
    'slope': [2, 1, 2, 2, 1, 0, 2, 1, 0, 2],
    'ca': [0, 1, 2, 1, 0, 2, 3, 4, 0, 1],
    'thal': [3, 2, 1, 3, 2, 2, 3, 1, 3, 3],
    'sex': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  
}

df = pd.DataFrame(data)

# Pie chart for Disease/No Disease distribution
disease_counts = df['target'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(disease_counts, labels=['Disease', 'No disease'], colors=['#1f77b4', '#ff7f0e'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Disease')
plt.legend(labels=['Disease', 'No disease'])
plt.show()

# Pie chart for Male-Female ratio
sex_counts = df['sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sex_counts, labels=['Male', 'Female'], colors=['#1f77b4', '#ff7f0e'], autopct='%1.1f%%', startangle=90)
plt.title('Male-Female Ratio')
plt.legend(labels=['Male', 'Female'])
plt.show()

# Bar chart for Heart Disease Frequency for Sex
df_grouped = df.groupby(['sex', 'target']).size().unstack()
df_grouped.plot(kind='bar', stacked=False, color=['#1f77b4', '#ff7f0e'], figsize=(8, 6))
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.ylabel('Count')
plt.legend(['No disease', 'Disease'])
plt.show()

# Define the number of rows and columns for the subplots
n_cols = 3
n_rows = int(len(df.columns) / n_cols) + 1

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))

# Flatten axes array for easy iteration
axes = axes.flatten()

# Plot histograms for each feature
for i, col in enumerate(df.columns):
    axes[i].hist(df[col], bins=30, edgecolor='black')
    axes[i].set_title(col)

# Remove any unused subplots
for i in range(len(df.columns), len(axes)):
    fig.delaxes(axes[i])

# Adjust layout
plt.tight_layout()
plt.show()
