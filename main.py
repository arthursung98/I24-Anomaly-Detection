import pandas as pd
import networkx as nx # for visualization
import matplotlib.pyplot as plt # for plotting
from Node import Node
from Edge import Edge
from test_zi import test_run_zi # for testing only

# Method to read CSV files as a DataFrame
def read_full_data(file_name, skiprows=0, index_col=False):
  df = pd.read_csv(file_name, skiprows=skiprows, index_col=index_col)
  df = df[['Frame #', 'ID', 'x', 'y', 'speed', 'acceleration']]

  return df

def test_run_arthur():
  input_directory = r"C:\I24 Motion Project\YB Outlier Detection\csv_data\TM_1000_GT.csv"
  
  # Checking to see if logic works for 1 csv file.
  df = read_full_data(input_directory, 0)
  max_frame = int(max(df['Frame #']))    # Find the maximum number of frame
  
  for i in range(max_frame) :
    # Take 1 frame during each loop to create a graph.
    one_frame_df = df.loc[(df['Frame #'] == i)]
    # TODO - Call GraphOneFrame

# TODO
# This method accepts a Pandas dataframe that represents 1 frame of the csv.
# It will translate the 
def graph_one_frame(one_frame_df) :
  # create a Graph obj
  # one_frame_df.map( for each car, add_node(car))
  
# test run code
if __name__ == "__main__":
  # test_run_arthur()
  test_run_zi()
  