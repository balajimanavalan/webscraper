import urllib.request
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import ssl

def send_mail(status):
    try:
        print("Logging in")
        s = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
        #s.set_debuglevel(1)
        msg = MIMEText(status)
        sender = 'emai_id'#g-mail id goes here
        recipients = ["e-mail-1's id", "e-mail-2's id"]
        msg['Subject'] = "GPU availability"
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        s.starttls()
        s.login(sender, "mail password")#mail_id's password goes here
        s.sendmail(sender, recipients, msg.as_string())
        s.quit()
        print("Message sent")

    except:
        print("Can't connect to the e-mail")


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url = input("Enter the URL For the product - ")
#print("Scrapping......")

while 1:
    try:
        url = "https://rptechindia.in/nvidia-geforce-rtx-3070.html"
        html = urllib.request.urlopen(url, timeout = 6, context = ctx).read()
        print("URL Connected", end=', ')
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('button')
        class_values = []
        for tag in tags:
            class_values.extend(tag.get('class', None))
            set(class_values)
        if 'tocart' in class_values:
            print("RTX 3070 Available now")
            send_mail("RTX 3070 Available now")
            break
        else:
            print("RTX 3070 out of stock\nRefreshing....")
    except:
        print("URL Unavailable\nReconnecting.......")
