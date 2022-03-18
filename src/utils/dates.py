from datetime import datetime


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except(ValueError):
        return False

def to_datetime(date_string):
    return datetime.strptime(date_string, "%d-%m-%Y")