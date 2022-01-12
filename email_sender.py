import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Antonio Franca'
email['to'] = 'joseantoniofi2000@gmail.com'
email['subject'] = 'trying shit'

email.set_content('good morning Manhattan')

with smtplib.SMTP(host='joseantoniofi2000@gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('joseantoniofi2000@gmail.com', 'password')
    smtp.send_message(email)
    print('all good bro')