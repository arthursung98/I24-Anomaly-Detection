from plot_graph import test_run_zi, generate_random_graph
import pandas as pd

if __name__ == "__main__":
    test_run_zi()
    
def read_full_data(file_name, skiprows=0, index_col=False):
    df = pd.read_csv(file_name, skiprows=skiprows, index_col=index_col)
    df = df[['Frame #', 'ID', 'x', 'y', 'speed', 'acceleration']]

    return df