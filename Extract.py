# this gathers the header columns for all project types in a PIT workbook
# a master file is created for each type using the header columns
# these will be appeneded to from each PIT CoC workbook

import pandas as pd
import os
from pathlib import Path
import csv


# file name to be created
file_PIT = "PIT_workbook_data_melted.csv"

# create a new master file with the header row, 
# if it already exists it will be deleted and a new one will be created
def create_master_file(excel_folder):

    global excel_data_folder
    excel_data_folder = excel_folder
    # print(f"This is the excel data folder: {excel_data_folder}")

    # path to the file to be deleted 
    file_path = Path(excel_data_folder) / file_PIT
    print(file_path) 
    try:
        # delete the file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print("CSV file deleted.")
        else:
            print("File not found.")
            
        # header row
        header = [
        'CoC', 'Project Type','Program ID',
        'County','PIT Date', 'Division',
        'Program',"PIT Count",'Data_point',
        'Amount']   
        
        # create a new file with the header row
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
       
    except FileNotFoundError:
        print("File does not exist")
    
    except PermissionError:
        print("No permission to delete this file")
       

    main_1()

    
def sheet_data(sheet_names, f):
       
    # open the PIT Excel file
    xls = pd.ExcelFile(f)

    # since all these made from templates
    # this will use the list of sheets names
    all_sheet_names = sheet_names
    
    # Loop through each sheet name in the list and process the data
    for each_sheet in all_sheet_names:
  
        # skip the first two rows of the sheet which are header rows 
        # and the third row which is empty
        df= pd.read_excel(f, sheet_name = each_sheet,skiprows=2)
        df.drop(df.index[0], inplace=True)
        df.reindex
        df.drop(df.index[0], inplace=True)

        # this will filter out any rows where either the "Program" or "CoC" columns are empty, 
        filtered_df = df[df['Program'].notna() & df['CoC'].notna()]

        # Melt the DataFrame to have a long format
        # List of columns to keep as id variables (not to melt)
        id_vars =list(filtered_df.columns)[:8]
        
        # List of columns to melt (the ones that contain the values)
        value_vars=list(filtered_df.columns)[8:]
            
        # Melt the DataFrame to have a long format
        df_melted = filtered_df.melt(id_vars=id_vars,value_vars=value_vars,var_name='Data_point',value_name='Amount')
     
        # append the melted DataFrame to the master file
        df_melted.to_csv(Path(excel_data_folder) / file_PIT, mode = "a", header=False, index=False)

def main_1():
 
    print(excel_data_folder)

    # loop through each PIT workbook in the directory
    for file_name in os.listdir(excel_data_folder):
        f = os.path.join(excel_data_folder, file_name)
       
        # check the file is a file and it ends with a zip extension
        if os.path.isfile(f) and file_name.startswith('NY-') and file_name.endswith('.xlsm'):
           
            # see each CoC code in the file name 
            print(file_name[:6])
            
            # the unshletered count is not included in the PIT workbook for said CoC 
            # all unsheltered counts across all CoCs are in the 'NY-' couple the year of the count
            # at the time of this writing it is 'NY-2026' workbook 
            # the file name starting with NY-20 will be used to identify the unsheltered count
            # only the 'Unsheltered' sheet will processed
            if file_name[:5] == 'NY-20':
                sheet_names = ['Unsheltered']
                sheet_data(sheet_names, f) 
            
            else:
                #  send all possible Excel sheet names
                sheet_names = ['Emergency','Safe Haven','Transitional']
                sheet_data(sheet_names, f)

    
    print("step 1 done")

# create_master_file()


