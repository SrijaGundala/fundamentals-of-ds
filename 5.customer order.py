import pandas as pd

data = {'Customer ID': [1, 2, 1, 3, 2],
        'Order Date': ['2023-01-15', '2023-02-10', '2023-01-25', '2023-03-05', '2023-02-20'],
        'Product Name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
        'Order Quantity': [3, 5, 2, 1, 4]}

order_data = pd.DataFrame(data)

customer_order_count = order_data['Customer ID'].value_counts()
print("Total number of orders made by each customer:\n", customer_order_count)

average_order_quantity = order_data.groupby('Product Name')['Order Quantity'].mean()
print("\nAverage order quantity for each product:\n", average_order_quantity)

earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
