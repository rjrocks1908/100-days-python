import requests
from datetime import datetime
import smtplib
import time

my_email = "rj.rahul1908@gmail.com"
password = "zsve lhmj uxqt kjoy"

MY_LAT = 28.704060
MY_LONG = 77.102493


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    sun_parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=sun_parameter)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="rockstarrahul.jain059@gmail.com",
                                msg="Subject:Look Up\n\nThe ISS is above you in the sky")
