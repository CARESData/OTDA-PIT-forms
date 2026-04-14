
## Purpose:
OTDA is asking us to fill in their PIT templates are each CoC by the the counties in them. 


### Prerequisite
  - PIT workbooks for all CoCS
- Unsheltered worbook for all CoCs
- OTDA templates
 
- Create folder to hold workbooks
- Create folder for OTDA templates


A pop form will ask where the 'Data' folder is located and the folder holding the OTDA templates 

### Extract.py
The script compiles all the files out into the ‘Data’ folder that begin with ‘NY-‘ and end with 'xlsx'. These are changed them into longitudinal data. 

### Transform.py
It processes the data by adding a coordinate (column and row) to each field name to be placed into the Excel template. Then it changes the structure to be used for the Excel templates.

### Break_apart.py
Creates individual files for each CoC. This was easier than creating new cold for the above.

### Insert.py
Place the data into the OTDA templates.










