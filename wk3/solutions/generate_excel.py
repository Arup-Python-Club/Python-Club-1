import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Awesome Sheet Name')

worksheet.write(0, 0, "X") # Cell (0, 0) is A1 (first row, first column)
worksheet.write(0, 1, "X^2") # Cell (0, 1) is B1 (first row, second column)

for x in range(101):
    worksheet.write(x + 1, 0, x)
    worksheet.write(x + 1, 1, x * x)

workbook.save('generated.xls')
