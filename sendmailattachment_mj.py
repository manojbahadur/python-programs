import smtplib 
import getpass
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

try:
	fromaddr = input("Enter the sender Email adress")
	toaddr = input("Enter the receivers Email adress") 
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 
	msg['To'] = toaddr 
	msg['Subject'] = input("Enter the subject")
	body = input("Enter the body of the program")
	msg.attach(MIMEText(body, 'plain')) 
	filename = "prithvireddy.jpeg"
	attachment = open("/home/al321/Downloads/prithvireddy.jpeg", "rb") 
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	password = getpass.getpass()
	s.login(fromaddr, password) 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text) 
except:
	print("some error occured")
else:
	print("Sent sucessfully")
s.quit() 
