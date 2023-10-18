import numpy as np
import pandas as pd
h= pd.read_csv("Housing.csv")
data = np.array(h)  
price =h["price"]
morethan4 = h[h["bedrooms"] > 4] 
average_price = np.mean(morethan4["price"]) 
print (" average sales price is " ,average_price)

