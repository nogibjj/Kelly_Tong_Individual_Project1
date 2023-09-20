import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

# This file includes all the functions created. 

#def load_data(data_path):
  #data = pd.read_csv(data_path)
  #return data

#def view_dataset(data_path): 
  #Auto = pd.DataFrame(data_path)
  #print(Auto.info())
  #print(Auto.head())
  #print(Auto.columns())

#def save_plot(name, data):
  #scatter_mpg(data).savefig("project1/visualization/" + f"plot_{name}.png")


def describe_dataset(data):
  #Auto = pd.DataFrame(data_path)
  df = pd.read_csv(data)
  #describe = data.describe()
  #markdown_describe = describe.to_markdown()
  return df.describe()





