
# This script takes the data from the 'ready_for_excel.csv' file, 
# which is created in the Transform.py script, 
# and breaks it into separate csv files for each CoC.
# which will then be used to fill in the OTDA Excel form for each CoC.

import pandas as pd
 
def break_part(directory):
    # directory for the compiled PIT data   
    dir_path = directory
        
    # file to look for in the directory 
    file = "ready_for_excel.csv"
    #  create variable for the file path to be used in the code 
    file_path = (f"{dir_path}\\{file}")

    # read in the csv file and create a list of the unique CoCs in the data
    df = pd.read_csv(file_path)
    
    # create a list of the unique CoCs in the data
    coc_list = df['CoC'].unique().tolist()

    # loop through the list of CoCs and filter the data for each CoC
    for coc in coc_list:
        # create a fltered based on coc
        filter = (df
            # filter rows
            .loc[(df['CoC'] == coc)]
            )
        # apply the filter to the data 
        result_discharged_positive = (filter)
        # save the result as a new csv file with the coc in the file name
        result_discharged_positive.to_csv(f"{dir_path}\\{coc}_filtered.csv", index=False)
