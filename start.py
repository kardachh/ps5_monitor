# start file
import time
from helper import get_current_time
from dictonary import words
from browser import open_browser,to_site,refresh_page
from notification import send_notification

driver = open_browser()
to_site(driver, words['sitePS5'])
input('\n\n\tВыбери свой город\n\tНажми Enter для старта\n\n')
in_process = True
while (in_process):
    refresh_page(driver)
    print(get_current_time())
    send_notification(words['title'], str(get_current_time()), 50)
    time.sleep(90)