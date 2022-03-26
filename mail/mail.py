import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def get_config(conf_file='conf.json'):
    
    with open(conf_file, encoding="utf-8") as file:
        config = json.load(file)
    
    return config


class myGMail():
    
    def __init__(self, login, password, header):
        self._login = login
        self._password = password
        self._header = header

    def sendMail(self, recipients, subject, message):
        port = 587
        GMAIL_SMTP = "smtp.gmail.com"

        msg = MIMEMultipart()
        msg['From'] = self._login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, port)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self._login, self._password)
        ms.sendmail(self._login, msg['to'], msg.as_string())

        ms.quit()
        #send end
        return None

    def receiveMail(self, folder_name = 'inbox'):
        GMAIL_IMAP = "imap.gmail.com"

        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self._login, self._password)
        mail.list()
        mail.select(folder_name)
        # criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        criterion = '(HEADER Subject "Test")'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        if result == 'OK':
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)     
        mail.logout()
        return email_message

if __name__ == '__main__':

    

    myLogin = get_config()['login']
    myPass = get_config()['pass']
    subject = 'Subject'
    recipients = get_config()['recipient']
    message = 'Message'
    header = None

    my_email = myGMail(myLogin, myPass, header)
    # my_email.sendMail(recipients, subject, message)
    message = my_email.receiveMail()
    print(message.get_payload())
