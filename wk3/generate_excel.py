import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Awesome Sheet Name')

worksheet.write(0, 0, "X") # Cell (0, 0) is A1 (first row, first column)
worksheet.write(0, 1, "X^2") # Cell (0, 1) is B1 (first row, second column)

# For each number X = 0 through 100, write X in the first column and X squared
# in the second column. Probably easiest with a for loop!

workbook.save('generated.xls')
