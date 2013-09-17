#!/usr/bin/python
# Send an email message using the STMP server at seaman@comsystem.us

from smtplib            import SMTP
from email.mime.text    import MIMEText
from sys                import stdin,argv

my_smtp     = 'smtp.webfaction.com'
my_user     = 'seaman'
my_password = 'mds959WF'
my_to       = ['mark.b.seaman@gmail.com']
my_from     = 'mark@seamanfamily.org'
my_subject  = 'Message from Mark Seaman'

def send_email(to_addrs, subject, text):
    if to_addrs=='': to_addrs = my_to
    from_addr =  my_from
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addrs[0]
    s = SMTP(my_smtp)
    s.login(my_user,my_password)
    s.sendmail(from_addr, to_addrs, msg.as_string())
    s.quit()

