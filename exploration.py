# import pandas
import pandas as pd

# code to allow script to run from terminal
if __name__ == "__main__":
    # read csv into dataframe
    data = pd.read_csv("/home/dq/scripts/data/CRDC2013_14.csv", encoding="Latin-1")
    # count jail schools
    jail_sch = data["JJ"].value_counts()
    # count clever schools
    clever_sch = data["SCH_STATUS_MAGNET"].value_counts()
    # print jail_sch
    print(jail_sch)
    # print clever_sch
    print(clever_sch)
    
    # now the pivot tavles to agreegate columns with a column as a reference and sum up the columns data
    
    # for jail schools explore male and females
    jail_pivot = pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index = "JJ", aggfunc = "sum")
    #  # for clever schools explore male and females
    clever_pivot =  pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index = "SCH_STATUS_MAGNET", aggfunc = "sum")
print (jail_pivot)
print (clever_pivot)

    
   
    
    
    
    
    
    
    
    
    
    
    

    