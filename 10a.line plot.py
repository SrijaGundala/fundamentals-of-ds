import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [15, 17, 20, 24, 28, 31, 32, 32, 30, 26, 21, 17]

plt.plot(months, temperature, marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature Over the Year')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

plt.show()
