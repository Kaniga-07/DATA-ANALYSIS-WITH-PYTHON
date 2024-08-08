import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("E:/MAINFLOW_INTERN/TASK_4/DATASET.csv", encoding='ISO-8859-1')

# 1. Overview of the dataset
print(data.info())

# 2. Descriptive statistics
print(data.describe(include='all'))

# 3. Distribution of Gender
sns.countplot(x='Gender', data=data)
plt.title('Distribution of Gender')
plt.show()

# 4. Age Distribution
sns.histplot(data['Age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.show()

# 5. Orders by Product Category
plt.figure(figsize=(10, 6))
sns.countplot(y='Product_Category', data=data, order=data['Product_Category'].value_counts().index)
plt.title('Orders by Product Category')
plt.show()

# 6. Total Amount spent by Gender
total_amount_by_gender = data.groupby('Gender')['Amount'].sum()
print(total_amount_by_gender)

# 7. Relationship between Orders and Amount
sns.scatterplot(x='Orders', y='Amount', hue='Gender', data=data)
plt.title('Relationship between Orders and Amount')
plt.show()
