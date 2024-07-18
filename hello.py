import pandas as pd
import boto3
import matplotlib.pyplot as plt

#pandas usage
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [20, 30, 35]}
df = pd.DataFrame(data)

print(df)

#matplotlib usage
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y, marker='o')

# Add title and labels
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()



#print("Hello world!")
