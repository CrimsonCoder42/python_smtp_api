import smtplib
import datetime as dt
import random
# -----------------------------------------------------------------------


current_time = dt.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.weekday()
print(type(day))

day_to_send = 4
# ----------------------------------------------------------------------

def create_quote():
    with open("quotes.txt") as file:
        quotes = [line for line in file]
        day_quote = quotes[random.randint(0, len(quotes) - 1)]
        return day_quote

# --------------------------------------------------------------------------


my_email = "python32testemail@gmail.com"
my_password = "gcwojpvcxrbjcnkc"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nostro37@gmail.com",
            msg=f"Subject: Hello \n\n {quote}"
        )
        connection.close()


if day == day_to_send:
    print("yes")
    new_quote = create_quote()
    send_email(new_quote)