import pandas as pd

data = {'property ID': [1, 2, 3, 4, 5],
        'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
        'number of bedrooms': [3, 4, 5, 3, 6],
        'area in square feet': [1500, 1800, 2200, 1600, 2500],
        'listing price': [250000, 320000, 400000, 280000, 450000]}

property_data = pd.DataFrame(data)

average_price_by_location = property_data.groupby('location')['listing price'].mean()
print("Average listing price of properties in each location:\n", average_price_by_location)

properties_with_more_than_four_bedrooms = property_data[property_data['number of bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_with_more_than_four_bedrooms)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)

property_with_largest_area = property_data[property_data['area in square feet'] == property_data['area in square feet'].max()]
print("\nProperty with the largest area:\n", property_with_largest_area)
