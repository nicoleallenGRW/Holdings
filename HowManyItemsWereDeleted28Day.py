# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:20:20 2018

@author: nallen
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:32:38 2018

@author: nallen
"""

# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
#
# Test being run to export shelf list to collection managers
# Email Excel Spreadhseet to manager and supervisor 
# Use XlsxWriter to create spreadsheet from SQL Query
# 
#

import psycopg2
import xlsxwriter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from datetime import datetime



excelfile =  'How Many Items Were Deleted and Created.xlsx'



#Set variables for email

emailhost = '172.21.1.47'
emailport = '25'
emailsubject = '[How Many Items Were Deleted & Created 28]'
emailmessage = '''The attached spreadsheet contains the items created last month, the total holdings, all ebooks created last month, all audiobooks created and all JUV items created. In order to calculate the total number of items deleted you must fill in the total holdings from the prior month in cell B2, B10 and B16.'''
emailfrom = 'nallen@greenwichlibrary.org'
emailto = ['nallen@greenwichlibrary.org','nallen@greenwichlibrary.org','SSchmidt@greenwichlibrary.org']
 #'nallen@greenwichlibrary.org','mburke@greenwichlibrary.org','SSchmidt@greenwichlibrary.org'

try:
    conn = psycopg2.connect("dbname=iii user=sqlaccess host=sierra-db port=1032 password=novelist_15 sslmode=require")
except psycopg2.Error as e:
    print ("Unable to connect to database: " + str(e))
    
cursor = conn.cursor()
cursor.execute(open("HowManyItemsWereDeleted28Day.sql","r",).read())
rows = cursor.fetchall()
conn.close()


workbook = xlsxwriter.Workbook(excelfile, {'remove_timezone': True})
worksheet = workbook.add_worksheet()


worksheet.set_landscape()
worksheet.hide_gridlines(0)



eformat= workbook.add_format({'text_wrap': True, 'valign': 'top' , 'num_format': 'mm/dd/yy'})
eformatlabel= workbook.add_format({'text_wrap': False, 'valign': 'top', 'bold': True})

#MAIN HOLDINGS NUMBERS

worksheet.set_column(0,0,49)
worksheet.set_column(1,1,15)
worksheet.set_column(2,2,15)
worksheet.set_column(3,3,15)




worksheet.set_header('HowManyItemsWereDeletedandCreated')

worksheet.write(1,0,'Main Holdings Prior Month', eformatlabel)
worksheet.write(2,0,'Items Created Last Month', eformatlabel)
worksheet.write(3,0,'All Main Items Deleted Last Month', eformatlabel)
worksheet.write(4,0,'Total Main Holdings', eformatlabel)
worksheet.write(5,0,'All ebook Bibs Created Last Month', eformatlabel)
worksheet.write(6,0,'All Audiobook Downloadable Bibs Created Last Month', eformatlabel)
worksheet.write(7,0,'All new JUV items created Last Month', eformatlabel)
worksheet.write(9,0,'BYR Holdings Prior Month', eformatlabel)
worksheet.write(10,0,'BYR Items Created Last Month', eformatlabel)
worksheet.write(11,0,'BYR All Items Deleted Last Month', eformatlabel)
worksheet.write(12,0,'BYR Total Holdings', eformatlabel)
worksheet.write(13,0,'All new BYR JUV items created last month', eformatlabel)
worksheet.write(15,0,'COS Holdings Prior Month', eformatlabel)
worksheet.write(16,0,'COS Items Created Last Month', eformatlabel)
worksheet.write(17,0,'COS All Items Deleted Last Month', eformatlabel)
worksheet.write(18,0,'COS Total Holdings', eformatlabel)
worksheet.write(19,0,'All new COS JUV items created last month', eformatlabel)

for rownum, col in enumerate(rows):
 
    worksheet.write(rownum+1,1,col[0])
    worksheet.write(rownum+2,1,col[1])
    
    worksheet.write(rownum+4,1,col[2])
    worksheet.write(rownum+5,1,col[3])
    worksheet.write(rownum+6,1,col[4])
    worksheet.write(rownum+7,1,col[5])
    worksheet.write(rownum+9,1,col[6])
    worksheet.write(rownum+10,1,col[7])
    worksheet.write(rownum+12,1,col[8])   
    worksheet.write(rownum+13,1,col[9])
    worksheet.write(rownum+15,1,col[10])
    worksheet.write(rownum+16,1,col[11])
    worksheet.write(rownum+18,1,col[12])
    worksheet.write(rownum+19,1,col[13])

    worksheet.write_formula('B4', "=(B2+B3)-b5") 
    worksheet.write_formula('B12', "=(B10+B11)-b13") 
    worksheet.write_formula('B18', "=(B16+B17)-b19")
   
workbook.close()


#Creating the email message
msg = MIMEMultipart()
msg['From'] = emailfrom
if type(emailto) is list:
    msg['To'] = ','.join(emailto)
else:
    msg['To'] = emailto
msg['Date'] = formatdate(localtime = True)
msg['Subject'] = emailsubject
msg.attach (MIMEText(emailmessage))
part = MIMEBase('application', "octet-stream")
part.set_payload(open(excelfile,"rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename=%s' % excelfile)
msg.attach(part)

#Sending the email message
smtp = smtplib.SMTP(emailhost, emailport)
smtp.sendmail(emailfrom, emailto, msg.as_string())
smtp.quit()








