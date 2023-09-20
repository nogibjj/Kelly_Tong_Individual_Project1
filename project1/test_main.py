#Check if the images and output markdown is generated
import os

def test_plot_save(self):
  file_to_check = 'scatter_mpg.png'
  self.assertTrue(os.path.exists("scatter_mpg.png"),f"The file '{file_to_check}' did not get created.")
