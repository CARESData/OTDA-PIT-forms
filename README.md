
##Purpose:
OTDA is asking for our help with the PIT count. Their templates are each CoC brotken out by the counties in them. 


#Data:

Copy the PIT workbooks for the above CoCs into the ‘Data’ folder. Also, add the ‘Unsheltered’ workbook along with the OTDA template. Make sure the template contains all the counties for each program that the PIT workbooks contain.

Extract_data_from_Excel_PIT_Workbooks.py
The script compiles all the files in the ‘Data’ folder that begin with ‘NY-‘ and changes them into longitudinal data. 

Transform_data_for_OTDA_Excel_workbook.py
It processes the data by adding a coordinate (column and row) to each field name to be placed into the Excel template. Then it groups the results by county. 

Insert_data_into_OTDA_PIT_Excel_template_by_county.py
Place the data into the OTDA template.










