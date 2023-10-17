import numpy as np
sales_data=np.array([100000,125000,1500000,175000])
total_sales=np.sum(sales_data)
percentage_increase=((sales_data[3]-sales_data[0])/sales_data[0])*100
print("Total sales of the year:",total_sales)
print("Percentage increase in sales=",percentage_increase)
