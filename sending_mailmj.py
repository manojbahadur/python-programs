#sending mail
import smtplib
try:
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender="manoj70195@gmail.com"
receiver="prathyushareddy1629@gmail.com"
msg="Hello"
s.login(sender,'pass')
s.sendmail(sender,recevier,msg)
except:
	print("uncessful")
s.quit()
