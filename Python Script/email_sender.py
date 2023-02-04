# Used to send email
import smtplib

# Used to construct email message contents
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email contents filename
filename = 'job_results.txt'

msg = MIMEMultipart("alternative")

# Open and read file, then process it to send as an email
with open(filename) as fp:
    msg = email.message.EmailMessage()
    msg.set_content(fp.read())

# Email info
msg['Subject'] = 'Binghamton CS Internships'
msg['From'] = 'BinghamtonInternships@gmail.com'
msg['To'] = 'BinghamtonInternships@gmail.com'

# Send the message
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(msg['From'], 'pasword')
s.send_message(msg)
s.quit()