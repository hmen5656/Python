import smtplib , sys , time
import getpass
import platform
import socket
import threading

def send_mail(mail,message):
    reload(sys)
    sys.setdefaultencoding("utf-8")

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("husmen5665","Abc123_+")

    try:
        server.sendmail("husmen5665@gmail.com",mail, message)
        server.close()
    except:
        pass

if __name__ =="__main__":
    send_mail("your@mail.com","message")
