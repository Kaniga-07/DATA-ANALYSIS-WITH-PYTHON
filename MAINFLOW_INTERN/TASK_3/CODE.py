import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700],
    'Expenses': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650],
    'Profits': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Sales'], color='blue', label='Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.legend()
plt.show()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', label='Sales')
plt.plot(df['Month'], df['Expenses'], marker='o', color='red', label='Expenses')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Sales and Expenses')
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(df['Month'], df['Profits'], color='green', label='Profits')
plt.xlabel('Month')
plt.ylabel('Profits')
plt.title('Monthly Profits')
plt.legend()
plt.show()
