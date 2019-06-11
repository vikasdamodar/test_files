#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# from_addr = 'vikazdmdr@gmail.com'
# to_addr = ['vikas.periyadath@tarams.com', 'vikas9142@gmail.com']
# msg = MIMEMultipart()
# msg['From'] = from_addr
# msg['To'] = ', '.join(to_addr)
# msg.attach(MIMEText("hiii", 'text'))
# msg['Subject'] = 'Issues, status changed to resolved'
#
# # Send the message via our own SMTP server.
# s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
# s.login("mbsupport@tarams.com", "mbsupport@123")
# s.sendmail(from_addr, to_addr, msg.as_string())
# s.quit()


class DataMissing(Exception):
    message = ""


import xlrd

# workbook = xlrd.open_workbook('c.xlsx')
# worksheet = workbook.sheet_by_name('sheet1')
# print([e for i, e in enumerate(worksheet.col_values(2))])

import pandas as pd
df = pd.read_excel('test_xlsx.xlsx')
f = df.to_dict(orient='records')
print(f)
df.index += 1
# null_columns=df.columns[df.isnull().any()]
# print(df)
# k = df[df.isnull().all(axis=1)][null_columns].head()


# empty_rows = set(df.index[df.isnull().all(axis=1)])
# print(empty_rows)
# data_missing_c = set(df.index[df['C'].isnull()]) - empty_rows
# data_missing_d = set(df.index[df['D'].isnull()]) - empty_rows
# print(data_missing_c, data_missing_d)
#
# data_type = df['C'].dtype == 'int64'
# print(data_type)
# print(df.dtypes)



# df.drop(df.index[[20,5]], inplace=True)
# print(df)
# df = df.reset_index(drop=True)
# print(df)

# print(df[df["c"].isnull()][null_columns])
import numpy as np
# index = df['c'].index[df['c'].apply(df.c.isnull())]
# k = ", ".join(str(i) for i in list(index))
# y = df['c'].index[df.loc[df.c.isnull()]]

