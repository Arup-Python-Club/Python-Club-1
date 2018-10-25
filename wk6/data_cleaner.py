import xlrd
import xlwt

# Read our input workbook
input_workbook = xlrd.open_workbook('data.xlsx')
input_sheet = input_workbook.sheet_by_index(0)

# Create our output workbook
output_workbook = xlwt.Workbook()
output_sheet = output_workbook.add_sheet('Sheet1')

# We want to clean the messy data, a very annoying and very common task
# Our input data has missing values, non-random large values, and strings mixed into random data
# We want to find those errors and replace the values in those cells with a new random decimal value
# You'll need to import "random" - a built in library to create random numbers


# Save our edited output workbook
output_workbook.save('clean_data.xls')
