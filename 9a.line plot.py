import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 15000, 13000, 16000, 18000]


plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Over Time (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)


plt.show()
