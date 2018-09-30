# import pandas
import pandas as pd

# code to allow script to run from terminal
if __name__ == "__main__":
    # read csv into dataframe
    data = pd.read_csv("/home/dq/scripts/data/CRDC2013_14.csv", encoding="Latin-1")
    # create a new column that adds the males and females
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    # compute the sum of males and females
    all_enrollment = data["total_enrollment"].sum()
    # compute percentage for males
    total_M = (data["TOT_ENR_M"].sum()/all_enrollment)*100
    # compute percentage for females
    total_F = (data["TOT_ENR_F"].sum()/all_enrollment)*100
    # compute percentage for Hispanic
    total_H = ((data["SCH_ENR_HI_M"].sum() + data["SCH_ENR_HI_F"].sum())/all_enrollment)*100
    # compute percentage for Hispanic
    total_AS = ((data["SCH_ENR_AS_M"].sum() + data["SCH_ENR_AS_F"].sum())/all_enrollment)*100
    # compute percentage for American indian
    total_AM = ((data["SCH_ENR_AM_M"].sum() + data["SCH_ENR_AM_F"].sum())/all_enrollment)*100
    # compute percentage for Hawaiian or Pasific Islander
    total_HP = ((data["SCH_ENR_HP_M"].sum() + data["SCH_ENR_HP_F"].sum())/all_enrollment)*100
    # compute percentage for Black
    total_BL = ((data["SCH_ENR_BL_M"].sum() + data["SCH_ENR_BL_F"].sum())/all_enrollment)*100
    # compute percentage for White
    total_WH = ((data["SCH_ENR_WH_M"].sum() + data["SCH_ENR_WH_F"].sum())/all_enrollment)*100
    # compute percentage for Two or more races
    total_TR = ((data["SCH_ENR_TR_M"].sum() + data["SCH_ENR_TR_F"].sum())/all_enrollment)*100
    
    # create a dictionary with races as keys and totals as values
    races = {"Male":total_M,"Female":total_F,"Hispanic":total_H,"American Indian":total_AM,"Asian":total_AS,"Hawaiian or Pasific Islander":total_HP,"Black":total_BL,"White":total_WH,"Two or more races":total_TR}
    
    # iterate through key values to print the dictionary
    
    for k,v in races.items():
        print("The ratio of total {} population is {}".format(k,v))
        
        
        
        
        