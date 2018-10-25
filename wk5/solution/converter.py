import xlrd
import xlwt

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

total = 0.0
for i in range(1, input_sheet.nrows):
    project_number = input_sheet.cell_value(rowx=i, colx=0)
    amount = float(input_sheet.cell_value(rowx=i, colx=1))
    currency = input_sheet.cell_value(rowx=i, colx=2)
    converted_amount = amount * exchange_rates[currency]
    output_sheet.write(i, 0, project_number)
    output_sheet.write(i, 1, converted_amount)
    total = total + converted_amount

output_sheet.write(input_sheet.nrows, 0, 'TOTAL')
output_sheet.write(input_sheet.nrows, 1, total)
output_workbook.save('converted.xls')

