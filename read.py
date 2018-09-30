# import pandas
import pandas as pd

# code to allow script to run from terminal
if __name__ == "__main__":
    # read csv into dataframe
    contents = pd.read_csv("/home/dq/scripts/data/CRDC2013_14.csv")
    # print first 5 lines
    print(contents.head())
    # explore the shape
    Count_Row=contents.shape[0] #gives number of row count
    Count_Col=contents.shape[1] #gives number of col count
    # print the shape3w
    print(Count_Row)
    print(Count_Col)
    
    
    




