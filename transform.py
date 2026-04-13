# This script transforms the data from the 'PIT_workbook_data_melted.csv' file, 
# which is created in the Extract.py script, and prepares it to be placed in the Excel form.
# The data is grouped by "County", "Proj. Type", and "Description" and the "Amount" is summed for each group. 
# The resulting dataframe is then merged with the coordinates for the Excel form, 
# which are stored in the "Form coordinates.xlsx" file.

import pandas as pd
from pathlib import Path


def main(file_directory):
 
    directory =  file_directory
    file_PIT = "PIT_workbook_data_melted.csv"

    # Get the data from the 'PIT_workbook_data_melted.csv'
    df_pit =pd.read_csv(Path(directory) / file_PIT)
  
    # Group the merged dataframe by "County", "Proj. Type", and "Description" and sum the "Amount" for each group. 
    # This will give us the total amount for each county, project type, and description.
    df_pit_ag = df_pit.groupby(['CoC','County', 'Project Type', 'Data_point'])['Amount'].sum().reset_index()

    # create df for the excel form coordinates
    df_coordinates =pd.read_excel(Path(directory) / "Form coordinates.xlsx")  
  
    # Merge the two dataframes on the "Program" column. Each program now has the county associated with it.
    df_result = pd.merge(df_pit_ag, df_coordinates, on=["Data_point", "Project Type"], how="left")
    df_filtered = df_result[df_result['col'].notna()]
    df_filtered.to_csv(Path(directory) / "ready_for_excel.csv", index=False)
    
    # print(df_result.dtypes)
    print()
    print()
    print("Step 2 done")


# main()