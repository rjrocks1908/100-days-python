import random
import smtplib
import datetime as dt
import pandas as pd

my_email = "rj.rahul1908@gmail.com"
password = "zsve lhmj uxqt kjoy"

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

letters = [f"letter_{i}.txt" for i in range(1, 4)]

for birthday in birthdays:
    receiver_email = birthday["email"]
    birthday_year = birthday["year"]
    birthday_month = birthday["month"]
    birthday_day = birthday["day"]

    current_dateTime = dt.datetime.now()

    if current_dateTime.month == birthday_month and current_dateTime.day == birthday_day:
        letter = random.choice(letters)
        with open(f"letter_templates/{letter}") as file:
            letter_content = file.read()
            letter_content = letter_content.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter_content}")
            print("Email Sent Successfully")
