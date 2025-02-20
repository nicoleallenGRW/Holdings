# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:32:38 2018

@author: nallen
"""

# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
#
# a item count by branch and material type
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



excelfile =  'HoldingsReportMainByramCosCob.xlsx' #Name the excel file you are creating


#Set variables for email
emailhost = 'xxx.xxx.x.xx' #Update for your email host
emailport = '25' #Update for your port
emailsubject = 'Holdings Report Main Byram & CosCob'
emailmessage = '''Here are the  Holdings for Main, Byram and Cos Cob. These numbers need to be copied into Arlene's spreadsheet. Updates were made in July 2022 to reflect more detailed reporting.'''
emailfrom = 'nallen@greenwichlibrary.org'
emailfrom = 'nallen@greenwichlibrary.org' #this is your email. It means staff can hit reply and contact you with questions.
emailto = ['nallen@greenwichlibrary.org', 'kfuscaldo@greenwichlibrary.org', 'jgaither@greenwichlibrary.org'] #this is the list of people you want the email to go to.

try:
    conn = psycopg2.connect("dbname=iii user=sqlaccess host=sierra-db port=1032 password=PASSWORD sslmode=require") #update this information for your specific location
except psycopg2.Error as e:
    print ("Unable to connect to database: " + str(e))
    
cursor = conn.cursor()
cursor.execute(open("holdingsreportmainByramCosCob.sql","r",).read())
rows = cursor.fetchall()
conn.close()


workbook = xlsxwriter.Workbook(excelfile, {'remove_timezone': True})
worksheet = workbook.add_worksheet()


worksheet.set_landscape()
worksheet.hide_gridlines(0)


eformat= workbook.add_format({'text_wrap': True, 'valign': 'top' , 'num_format': 'mm/dd/yy'}) #basic information that controls the display of your spreadsheet -ex. how dates are formated and whether anything is bolded-
eformatlabel= workbook.add_format({'text_wrap': False, 'valign': 'top', 'bold': True})
# sets the width of your columns (notice that in Python spreadsheets start with row and column 0


worksheet.set_column(0,0,25)
worksheet.set_column(1,1,15)
worksheet.set_column(2,2,15)
worksheet.set_column(3,3,15)


#Creates all the column & row headings

worksheet.set_header('HoldingsReportMainByram&CosCob')

worksheet.write(1,0,'Adult Books', eformatlabel) #row heading
worksheet.write(2,0,'Music CDs', eformatlabel) #row heading
worksheet.write(3,0,'Music Downloadable', eformatlabel) #row heading
worksheet.write(4,0,'Audiobook CDs', eformatlabel)
worksheet.write(5,0,'Audiobook Downloadable', eformatlabel)
worksheet.write(6,0,'Videos Downloadable', eformatlabel)
worksheet.write(7,0,'DVDs', eformatlabel)
worksheet.write(8,0,'Lending Art', eformatlabel)
worksheet.write(9,0,'Museum Passes', eformatlabel)
worksheet.write(10,0,'Innovation Lab Kits', eformatlabel)
worksheet.write(11,0,'', eformatlabel)
worksheet.write(12,0,'YA Books', eformatlabel)
worksheet.write(13,0,'YA eBooks', eformatlabel)
worksheet.write(14,0,'YA Audiobook Downloadable', eformatlabel)
worksheet.write(15,0,'YA Games', eformatlabel)
worksheet.write(16,0,'', eformatlabel)
worksheet.write(17,0,'Juv Books', eformatlabel)
worksheet.write(18,0,'Juv eBooks', eformatlabel)
worksheet.write(19,0,'Juv Music CDs', eformatlabel)
worksheet.write(20,0,'JUV Audiobooks', eformatlabel)
worksheet.write(21,0,'JUV Audiobooks Downloadable', eformatlabel)
worksheet.write(22,0,'Juv DVDs', eformatlabel)
worksheet.write(23,0,'JUV Games', eformatlabel)
worksheet.write(24,0,'JUV LaunchPads & Kits', eformatlabel)
worksheet.write(0,1,'Main', eformatlabel) #column heading
worksheet.write(0,2,'BYR', eformatlabel) #column heading
worksheet.write(0,3,'COS', eformatlabel) #column heading

#places the data from your SQL into specific cells. Each data point is listed in order in the brackets starting with 0
for rownum, col in enumerate(rows):
 
    worksheet.write(rownum+1,1,col[0])
    worksheet.write(rownum+2,1,col[1])
    worksheet.write(rownum+3,1,col[2])
    worksheet.write(rownum+4,1,col[3])
    worksheet.write(rownum+5,1,col[4])
    worksheet.write(rownum+6,1,col[5])
    worksheet.write(rownum+7,1,col[6])
    worksheet.write(rownum+8,1,col[7])
    worksheet.write(rownum+9,1,col[8]) 
    worksheet.write(rownum+10,1,col[9]) #Innovation Lab kit
    worksheet.write(rownum+15,1,col[10]) #YA games
    worksheet.write(rownum+17,1,col[11]) #Juv Books    
    worksheet.write(rownum+19,1,col[12])    
    worksheet.write(rownum+20,1,col[13])
    worksheet.write(rownum+22,1,col[14])
    worksheet.write(rownum+23,1,col[15])
    worksheet.write(rownum+24,1,col[16])    
    
    worksheet.write(rownum+1,2,col[17])
    worksheet.write(rownum+2,2,col[18])
    worksheet.write(rownum+3,2,col[19])
    worksheet.write(rownum+4,2,col[20])
    worksheet.write(rownum+5,2,col[21])
    worksheet.write(rownum+6,2,col[22])
    worksheet.write(rownum+7,2,col[23])
    worksheet.write(rownum+8,2,col[24])
    worksheet.write(rownum+9,2,col[25]) 
    worksheet.write(rownum+10,2,col[26]) #Innovation Lab kit
    worksheet.write(rownum+15,2,col[27]) #YA games
    worksheet.write(rownum+17,2,col[28]) #Juv Books    
    worksheet.write(rownum+19,2,col[29])    
    worksheet.write(rownum+20,2,col[30])
    worksheet.write(rownum+22,2,col[31])
    worksheet.write(rownum+23,2,col[32])
    worksheet.write(rownum+24,2,col[33])     
       
    worksheet.write(rownum+1,3,col[34])
    worksheet.write(rownum+2,3,col[35])
    worksheet.write(rownum+3,3,col[36])
    worksheet.write(rownum+4,3,col[37])
    worksheet.write(rownum+5,3,col[38])
    worksheet.write(rownum+6,3,col[39])
    worksheet.write(rownum+7,3,col[40])
    worksheet.write(rownum+8,3,col[41])
    worksheet.write(rownum+9,3,col[42]) 
    worksheet.write(rownum+10,3,col[43]) #Innovation Lab kit
    worksheet.write(rownum+15,3,col[44]) #YA games
    worksheet.write(rownum+17,3,col[45])     
    worksheet.write(rownum+19,3,col[46])    
    worksheet.write(rownum+20,3,col[47])
    worksheet.write(rownum+22,3,col[48])
    worksheet.write(rownum+23,3,col[49])
    worksheet.write(rownum+24,3,col[50])

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








