#Check if the images and output markdown is generated
import os

def test_save_plot():
  assert os.path.exists("scatter_mpg.png")
