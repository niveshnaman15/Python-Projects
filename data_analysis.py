
# Data Analysis with Pandas
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'customer': ['A', 'B', 'C', 'D'], 'sales': [200, 120, 340, 560]}
df = pd.DataFrame(data)

# Calculate average sales
average_sales = df['sales'].mean()
print("Average Sales:", average_sales)

# Plot sales data
df.plot(kind='bar', x='customer', y='sales', title='Customer Sales')
plt.show()
