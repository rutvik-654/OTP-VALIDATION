import smtplib 
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n=int(input('Number of emails:'))
l=[]
for i in range(n):
    x=input('Enter emails')
    l.append(x)

for i in l:
  otp = random.randint(1111,9999)
  msg = MIMEMultipart()
  body=f"OTP for Verification {otp}"
  msg["From"] = "rutvik.yedla@gmail.com"
  msg["TO"] = i
  msg["Subject"]="OTP for Validation"
  msg.attach(MIMEText(body,'plain'))

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login("rutvik.yedla@gmail.com","izxg nsex qasn yrbm")
  server.send_message(msg)
  server.quit()

  cotp=int(input("Enter OTP: "))

  if otp==cotp:
    print("OTP Validation Successful")

  else:
     print("Invalid OTP")
