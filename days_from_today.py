import datetime as dt

def get_days_from_today(date: str) -> int:
    try:
        date = dt.datetime.strptime(date, '%Y-%m-%d').date()
    except (ValueError, TypeError) :
        return 'Not Valid formt! Should be YYYY-MM-DD as string'

    today = dt.date.today()
    days_from_date = (today - date).days
    
    return days_from_date