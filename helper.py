import datetime

def get_current_time():
    date = datetime.datetime.now()
    return date.strftime('%d-%m-%Y %H:%M:%S')