import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

# This file includes all the functions created. 

def load_data(data_path)
  data = pd.read_csv(data_path)
  return data

def view_dataset(data_path): 
  Auto = pd.DataFrame(data_path)
  print(Auto.info())
  print(Auto.head())
  print(Auto.columns())

def save_plot(name, data):
  scatter_mpg(data).savefig("project1/visualization/" + f"plot_{name}.png")


def describe_dataset(data_path):
  #Auto = pd.DataFrame(data_path)
  describe = data_path.describe()
  markdown_describe = describe.to_markdown()
  return markdown_output

def scatter_mpg(data_path):
  Auto = data_path
  # Create the scatter plot
  plt.figure(figsize=(10, 6))
  plot = sns.scatterplot(data = Auto, x = 'weight', y = 'mpg', hue = 'origin')
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('MPG')
  plt.title('Correlation between Vehicle Weight and MPG based on origin')
  
  # Show the plot
  plt.show()
  return plot

def fitted_mpg():
  Auto = data_path
  
  plt.figure(figsize=(10, 6))
  sns.lmplot(data=Auto, x='weight', y='mpg', hue='origin', height=6, aspect=2)
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('MPG')
  
  # Show the plot
  plt.show()

def scatter_acc():
  Auto = data_path
  
  # Create the scatter plot
  plt.figure(figsize=(10, 6))
  sns.scatterplot(data = Auto, x = 'weight', y = 'acceleration', hue = 'year')
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('Acceleration')
  plt.title('Correlation between Vehicle Weight and acceleration based on year')
  
  # Show the plot
  plt.show()

def fitted_acc():
  Auto = data_path
  
  plt.figure(figsize=(10, 6))
  sns.lmplot(data=Auto, x='weight', y='acceleration', hue='year', height=6, aspect=2)
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('Acceleration')
  
  # Show the plot
  plt.show()

