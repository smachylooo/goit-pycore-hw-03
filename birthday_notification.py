import datetime as dt
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    res = []
    today = dt.datetime.today().date()
    for user in users:
        birthday_this_year = dt.datetime.strptime(user['birthday'], '%Y.%m.%d').date().replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_diff = (birthday_this_year - today).days
        if 0 < days_diff <= 7:
            shift_days = {5: 2, 6: 1}.get(birthday_this_year.weekday(), 0)
            birthday_this_year += dt.timedelta(days=shift_days)

            res.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d"),
            })

    return res