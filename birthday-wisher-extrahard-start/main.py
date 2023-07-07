##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

# https://www.pythonanywhere.com/
current_time = dt.datetime.now()
CURRENT_YEAR = current_time.year
CURRENT_MONTH = 7
CURRENT_DAY = 7

# 1. Update the birthdays.csv

def update_csv(*args):
    name = args[0]
    email = args[1]
    year = args[2]
    month = args[3]
    day = args[4]

    df = pd.DataFrame({
        'name': [name],
        'email': [email],
        'year': [year],
        'month': [month],
        'day': [day]
    })

    df.to_csv('birthdays.csv', mode='a', header=False, index=False)


# 2. Check if today matches a birthday in the birthdays.csv

def check_bday():
    df = pd.read_csv('birthdays.csv')
    # Loop through data row
    for index, row in df.iterrows():
        if CURRENT_MONTH == row["month"] and CURRENT_DAY == row["day"]:
            return [True,row]
    return [False,"No Bday today"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

def random_letter(name):
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    rand_choice = letters[random.randint(0, len(letters) - 1)]
    with open(f"letter_templates/{rand_choice}", "r") as data:
        content = data.read()
        custom_letter = content.replace('[NAME]', name)
        return custom_letter




# 4. Send the letter generated in step 3 to that person's email address.

def send_email(email, content):
    my_email = "python32testemail@gmail.com"
    my_password = "gcwojpvcxrbjcnkc"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Hello \n\n {content}"
        )
        connection.close()

row_data = check_bday()


if row_data[0]:
    bday_data = row_data[1]
    name = row_data[1]["name"]
    email = row_data[1]["email"]
    year = row_data[1]["year"]
    month = row_data[1]["month"]
    day = row_data[1]["day"]
    content = random_letter(name)
    send_email(email, content)
