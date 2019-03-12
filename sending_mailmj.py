import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	sender='python.program27@gmail.com'
	receiver='manoj70195@gmail.com'
	msg='hello'
	s.login(sender,"python.program#277")
	s.sendmail(sender,receiver,msg)
except:
	print('some error occured')
else:
	print('message sent sucessful')
	s.quit()
