# Used to send email
import smtplib

# Used to construct email message contents
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# firebase stuff

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Python Script/secret-key.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

ref = firestore_client.collection('emails').document('email-list')

# Make email object
msg = MIMEMultipart("alternative")

# Email info
msg['Subject'] = 'Binghamton CS Internships'
msg['From'] = 'BinghamtonInternships@gmail.com'
msg['To'] = 'BinghamtonInternships@gmail.com'

# Create the plain-text and HTML version of the message
text = text = """ \
Binghamton Internship Newsletter

Below are last week's CS Internships:

"""

html = ""
with open("Python Script/email_template.html") as fp:
    html += fp.read()[:-233]

# Email contents filename
filename = 'Python Script/job_results.txt'

# Open and read file, then process it to send as an email
with open(filename) as fp:
    text += fp.read()

with open(filename) as fp:
    lines = fp.readlines()
    i = 0
    for line in lines:
        if i % 8 == 0:
            if line == "":
                html += "<div>"
            else:
                html += "<div><img src='%s' class='thumbnail'>" % line
        elif i % 8 == 1:
            html += "<h3>%s</h3>" % line
        elif i % 8 >= 2 and i % 8 <= 5:
            html += "<p>%s</p>" % line
        elif i % 8 == 6:
            html += "<p><a href='%s'>View job listing</a></p>" % line
        elif i % 8 == 7:
            html += "</div><hr>"
        i += 1

text += """ \

Newsletter created by Emma Topolovec
GitHub: https://github.com/EmmaTopolovec
Unsubscribe: https://google.com
"""
html += """\
        <div>
            <p>Newsletter created by <a href="https://github.com/EmmaTopolovec">Emma Topolovec</a></p>
            <a href="https://binghamton.web.app/unsubscribe.html">Unsubscribe</a>
        </div>

    </body>
</html>"""

# Turn these into plain/html MIMEText objects
plain_email = MIMEText(text, "plain")
html_email = MIMEText(html, "html")

# Attach to MIMEMultipart message
msg.attach(plain_email)
msg.attach(html_email) # email will attempt to render this first

# Send the message
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(msg['From'], 'password')
all_emails = []
for addr in ref.get().to_dict()['arrayField']:
    all_emails = all_emails + [addr]
print(all_emails)
s.send_message(msg, msg['From'], [msg['To']] + all_emails)
s.quit()