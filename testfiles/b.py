# import PyPDF2
#
#
# import textract
# text = textract.process("/home/vikas/Downloads/today.pdf")
# print(text.decode('utf-8'))
#
# with open('j.txt', 'r+') as f:
#     f.writelines(text.decode('utf-8'))

import xlwt
from xlutils.copy import copy


workbook = xlwt.Workbook()
sheet = workbook.add_sheet('sheet1')
sheet.write(0,0, "A")
sheet.write(0,1, "B")
sheet.write(0,2, "C")
sheet.write(0,3, "D")

for i in range(1, 500):
    if i in [6,7,8,9,20]:
        pass
    else :
        sheet.write(i, 0, 'test')
for i in range(1, 500):
    if i in [6,7,8,9,20]:
        pass
    else :
        sheet.write(i, 1, 'test')
for i in range(1, 500):
    if i in [3,6,7,8,9,20,25]:
        pass
    else:
        sheet.write(i, 2, 'test')
for i in range(1, 500):
    if i in [6,7,8,9,17,20,29,56]:
        pass
    else:
        sheet.write(i, 3, 'test')

workbook.save('c.xlsx')

# import pandas as pd
# df = pd.read_excel('c.xlsx')
# print(df)