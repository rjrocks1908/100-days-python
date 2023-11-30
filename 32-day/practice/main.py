import smtplib
import datetime as dt
import random

my_email = "rj.rahul1908@gmail.com"
password = "zsve lhmj uxqt kjoy"

with open("quotes.txt") as file:
    quotes_data = file.readlines()
    quote = random.choice(quotes_data)

    now = dt.datetime.now()

    if now.weekday() == 3:
        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user=my_email, password=password)
            connections.sendmail(from_addr=my_email, to_addrs="rockstarrahul.jain059@gmail.com", msg=quote)
            print("Email send successfully")
    else:
        print("Today is not the day!")
