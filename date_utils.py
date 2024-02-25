import time


def is_in_future(date):
    date_in_seconds = time.mktime(time.strptime(date, "%Y-%m-%d"))
    return date_in_seconds > time.time()


def add_years(date, years):
    return str(int(date[:4]) + years) + date[4:]
