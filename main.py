import datetime as dt
import random
import smtplib

import pandas

my_email = "your_email@yahoo.com"
password = "your_password"

today = dt.datetime.now()
day = today.day
month = today.month
year = today.year

df = pandas.read_csv("birthdays.csv")
birthday_dict = {row['name']:(row.month, row.day) for (index, row) in df.iterrows()}
birthday_email = {email['name']:email.email for (name, email) in df.iterrows()}

def send_email():
    with open(".././quotes.txt") as file:
        lines = file.read().splitlines()
        random_quote = random.choice(lines)


    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email[f"{key}"], msg=("From: your_email@yahoo.com\n"
                                                                                         "To: birthdayemail@yahoo.com]\n"
                                                                                         "Subject: Quote of the day\n"
                                                                                         "\n"
                                                                                         f"Today is {month}/{day}/{year}, Happy Birthday {key}!!! Here's some wisdom for your special day: {random_quote}"
                                                                                         ))



for (key, value) in birthday_dict.items():
    if value == (month, day):
      
        send_email()
