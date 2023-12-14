import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook("副本Geo-AI ethics cases(1).xlsx")
sheet = workbook.active

# Get the titles from the first row and convert them to lowercase
for cell in sheet[1]:
    try:
        cell.value = cell.value.lower()
    except:
        pass

# Save the workbook to a new file
output_path = "modified_geo_ai_ethics_cases.xlsx"
workbook.save(output_path)