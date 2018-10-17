import xlrd
import xlwt

# Hardcoded for today, could retrieve dynamically if you want to get fancy
# (e.g. check out fixer.io)
exchange_rates = {
    'CAD': 0.77,
    'EUR': 1.16,
    'JPY': 0.0089,
    'GBP': 1.32,
    'AUD': 0.71,
    'USD': 1.0
}

input_workbook = xlrd.open_workbook('projects.xlsx')
input_sheet = input_workbook.sheet_by_index(0)

output_workbook = xlwt.Workbook()
output_sheet = output_workbook.add_sheet('Sheet1')
output_sheet.write(0, 0, 'Project')
output_sheet.write(0, 1, 'Income')

output_workbook.save('converted.xls')

# Additional tasks if you are able to convert everything to USD:
# - Find the average project income and write that below the total
# - Convert the new cost column to USD and find the total cost
# - What is the profit % of this portfolio? ((revenue-cost)/revenue)
# - Print out the projects that aren't profitable

##### USEFUL RESOURCES/NOTES #####

# xlrd: https://github.com/python-excel/xlrd
# xlwt: https://pypi.org/project/xlwt/

# General tip: don't try to do everything all at once! Do a step or two, then
# print out something temporary to check if you're on the right track

# You can give *two* arguments to range() if you don't want to start at zero -
# range(2, 5) will give you [2, 3, 4], range(1, 4) will give you [1, 2, 3] etc.

# Remember that row and column indices generally start at 0, not 1!

##### SUGGESTED OUTLINE #####

# Open the projects.xlsx workbook with xlrd and get its first sheet

# Create a new workbook with xlwt and add a new sheet to it

# Add 'Project' and 'Income' header cells to the output sheet

# Loop through input sheet rows (not including the header row!)
# Get the project number, amount and currency name from each row
#   - Pause at this point and just print out these values to make sure you're
#     reading them correctly before trying to do stuff with them
# Convert to USD using the exchange_rates dict
# Write the project number and converted amount to the output sheet
# Add the converted amount to a running total

# Add a 'TOTAL' row to the output sheet with the total income amount
# Save the output workbook to converted.xls
