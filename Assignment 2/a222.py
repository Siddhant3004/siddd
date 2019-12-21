import openpyxl
# Load the xlsx file by using path or name
wb = openpyxl.load_workbook("Assignment2.xlsx")
# Get workbook active sheet
sheet = wb.active
# Iterate through rows
for i in range(1,11):
    # Iterate through columns
    for j in range(1,27):
        # Assign value to specific cell
        sheet.cell(row=i,column=j).value=chr(64+j)+str(i)
# Save the xlsx file        
wb.save('Assignment2.xlsx') 