import smtplib # to create a SMTP server
from email.message import EmailMessage

email = EmailMessage()

email['from'] = '' # email (from)
email['to'] = [''] # email/emails (to)
email['subject'] = '' # email subject
email.set_content('') # email message

with smtplib.SMTP(host = '', port = 587) as smtp: # param1: SMTP server, param2: port
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '') # param1: 'email', param2: 'password'
    smtp.send_message(email)
    print('All done!')

# SMTP server (google): host = 'smtp.gmail.com'
# SMTP server (outlook): host = 'smtp-mail.outlook.com'
