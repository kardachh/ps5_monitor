from plyer import notification
def send_notification(_title, _message,_timeout):
        notification.notify(
        title = _title,
        message = _message,
        timeout = _timeout,
        app_name = "PS5 Monitor"
        )