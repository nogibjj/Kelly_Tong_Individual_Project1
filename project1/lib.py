import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

# This file includes all the functions created. 


def view_dataset(data_path): 
  Auto = pd.DataFrame(data_path)
  print(Auto.info())
  print(Auto.head())
  print(Auto.columns())


def describe_dataset(data_path):
  #Auto = pd.DataFrame(data_path)
  describe = data_path.describe()
  markdown_describe = describe.to_markdown()
  return markdown_output

