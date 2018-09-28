import xlwt

def greeting(name):
    return 'Hello, ' + name + '!'

jared_greeting = greeting('Jared')
nigel_greeting = greeting('Nigel')

print(jared_greeting)
print(nigel_greeting)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Greetings')
worksheet.write(0, 0, jared_greeting)
worksheet.write(1, 0, nigel_greeting)
workbook.save('greetings.xls')
