from datetime import date
from bday_messages import random_message

today = date.today()
next_birthday = date(2025, 4, 10)

days_away = next_birthday - today
days_away = days_away.days

if today == next_birthday:
    print(random_message)
else:
    print(f'My next birthday is {days_away} days away!')
