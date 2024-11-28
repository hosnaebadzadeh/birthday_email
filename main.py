
import os
import pandas as pd
import smtplib
from datetime import datetime
import random
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
myem = os.getenv('MYEM')
mypass = os.getenv('MYPASS')

texts = ['text1.txt', 'text2.txt', 'text3.txt']
data = 'info.csv'

friends_df = pd.read_csv(data)
today = datetime.now().date()

for index, row in friends_df.iterrows():
    friname = row['name']
    friemail = row['email']
    birthdate = datetime.strptime(row['birthday'], "%Y/%m/%d").date()


    if birthdate.month == today.month and birthdate.day == today.day:
        chose = random.choice(texts)
        with open(chose, "r") as mesg:
            rfile = mesg.read()
        fmsg = rfile.replace("[Name]", friname)
        msg = MIMEMultipart()
        msg["From"] = myem
        msg["To"] = friemail
        msg["Subject"] = "Happy Birthday!"
        msg.attach(MIMEText(fmsg, "plain", "utf-8"))

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=myem, password=mypass)
            connection.sendmail(
                from_addr=myem,
                to_addrs=friemail,
                msg=msg.as_string()
            )

        print(f"today is {friname} birthday")
    else:
        print(f"today is not {friname} birthday.")

# https://github.com/hosnaebadzadeh