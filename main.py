
from bye import main_bye
from Extract import create_master_file
from transform import main as transform_main
from Break_apart import break_part
from Insert import loop_through_csv
import awards_submit_form 


def main():
    
    # call the awards_submit_form to get the 
    # folders for the AWARDS data and the Excel file
    awards_submit_form.main()
   
    
    # create global variable to pass along
    global pull_directory
    global excel_directory
    
    # call the function to get the location for each folder
    pull_directory = awards_submit_form.awards_file()
    excel_directory = awards_submit_form.excel_file()
   

main()
create_master_file(pull_directory)
transform_main(pull_directory)
break_part(pull_directory)
loop_through_csv(pull_directory, excel_directory)
main_bye()



