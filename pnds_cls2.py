# pandas files 2
import pandas as pd
df = pd.DataFrame({
    "product" : ["mobile", "laptop", "cart", "bike", "car"],
    "price" : [100, None, 400, 500, 600],
    "quantity" : [3, 5, 6, 1, None]
    
})
print(df)
print(df.dropna()) #removes the null elements
print(df.describe())
