# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("abdul.16it@cmr.edu.in", "aliabdul7") 

# message to be sent 
message = "hello abdul"

# sending the mail 
s.sendmail("abdul.16it@cmr.edu.in", "abdul.16it@cmr.edu.in", message) 

# terminating the session 
s.quit() 
