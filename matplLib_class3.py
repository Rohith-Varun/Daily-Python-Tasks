#Pie Charts

import matplotlib.pyplot as p
fruits = ["Mango", "Apple", "Banana", "Papayya", "Orange"]
quantity = [20, 60, 40, 4, 10]

p.pie(quantity, labels = fruits)
#p.pie(quantity, labels = fruits, autopct="%1.1f%%")#for percentages
p.show()