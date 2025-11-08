from datetime import datetime, date, timedelta

# Функція перетворює рядок у форматі "YYYY.MM.DD" у об’єкт datetime.date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

# Функція перетворює об’єкт типу date назад у рядок "YYYY.MM.DD"
def date_to_string(date):
    return date.strftime("%Y.%m.%d")

# Функція готує список користувачів: 
# замінює текстові дати народження на об’єкти типу date
def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

# Знаходить наступний день тижня (weekday) після start_date
# weekday: 0=понеділок, ..., 6=неділя
def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

# Якщо день народження припадає на вихідний (субота=5, неділя=6),
# повертає дату наступного понеділка, інакше оригінальну дату
def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

# Основна функція: отримує список користувачів із днями народження (datetime.date),
# повертає список користувачів, чиї дні народження настають за 'days' днів з урахуванням перенесень у випадку вихідних
def get_upcoming_birthdays(users, days=7, today = None):
    upcoming_birthdays = []
    # Використовуємо сьогоднішню дату, якщо не задано явно (зручно для продуктивного використання)
    if today is None:
       today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        congratulation_date = adjust_for_weekend(birthday_this_year)

        if 0 <= (congratulation_date - today).days <= days:
            congratulation_date_str = date_to_string(congratulation_date)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.11.09"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
prepared_users = prepare_user_list(users)
upcoming = get_upcoming_birthdays(prepared_users, days=7)

for user in prepared_users:
    birthday_this_year = user["birthday"].replace(year=today.year)
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    congratulation_date = adjust_for_weekend(birthday_this_year)
    delta_days = (congratulation_date - today).days

    print(f"User {user['name']} birthday this year: {birthday_this_year}, congratulation date: {congratulation_date}, days_until: {delta_days}")
