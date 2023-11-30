import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file using pandas
df = pd.read_csv(r"C:\Users\HP\Desktop\Python\ritik.csv")

# Plotting the bar graph
plt.bar(df['Levels'], df['Numbers_of _Students'], color='skyblue')

# Adding labels and title
plt.xlabel('Levels')
plt.ylabel('Number of Students')
plt.title('Distribution of Students by Level')

# Display the plot
plt.show()

