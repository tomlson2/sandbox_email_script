import smtplib
import pandas as pd

SENDER = 'thomasmbryson@gmail.com'
PASSWORD = ''

df = pd.read_csv('swe.csv')
df['Name'] = df['Name'].str.split(' ').str[0]
df = df[~df['Email'].isnull()]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(SENDER, PASSWORD)

subject = 'Reaching out -- Sandbox'
with open("email_content.txt") as f:
    email_body = f.read()

for index, row in df.iterrows():
    name = row['Name']
    receiver = row['Email']
    greeting = f'Hi {name},\n\n'
    email = f'Subject: {subject}\n\n{greeting}{email_body}'
    server.sendmail(SENDER, receiver, email)
