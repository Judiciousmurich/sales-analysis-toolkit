import matplotlib.pyplot as plt
import seaborn as sns
# Bar plot for total sales by product
plt.figure(figsize=(10, 6))
sns.barplot(data=summary, x='Product', y='TotalSales')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()