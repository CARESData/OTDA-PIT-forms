
## Purpose:
OTDA is asking us to fill in their PIT templates are each CoC by the the counties in them. 


### Prerequisite
  - PIT workbooks for all CoCS
- Unsheltered worbook for all CoCs
- OTDA templates
 
- Create folder to hold workbooks - Data
- Create folder for OTDA templates - Template


A form will ask where the workbook folder (Data) and the folder holding the OTDA templates (Template) are located. 

### Extract.py
The script combines all the files out into the ‘Data’ folder into one csv file.  

### Transform.py
The file created above is merged with a file with a coordinate (column and row) to each field name to be placed into the Excel template. Then it changes the structure to be used for the Excel templates.

### Break_apart.py
Breaks apart the file above into individual files for each CoC. 

### Insert.py
Place the data for each CoC into their respective OTDA templates.










