#Check if the images and output markdown is generated
import os
import data from main

def test_data():
  assert data is not None

def test_save_plot():
  assert os.path.exists("scatter_mpg.png")

def test_save_plot2():
  assert os.path.exists("fitted_mpg.png")

def test_save_plot3():
  assert os.path.exists("scatter_acc.png")

def test_save_plot4():
  assert os.path.exists("fitted_mpg.png")

def test_save_markdown():
  assert os.path.exists("desc_stats.md")
