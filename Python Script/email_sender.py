# Used to send email
import smtplib

# Used to construct email message contents
import email

# Email contents filename
filename = 'test_file.txt'

# Open and read file, then process it to send as an email
with open(filename) as fp:
    msg = email.message.EmailMessage()
    msg.set_content(fp.read())

# Email info
msg['Subject'] = f'The contents of {filename}'
msg['From'] = 'BinghamtonInternships@gmail.com'
msg['To'] = 'BinghamtonInternships@gmail.com'

# Send the message
# s = smtplib.SMTP('localhost')
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(msg['From'], 'password')
s.send_message(msg)
s.quit()