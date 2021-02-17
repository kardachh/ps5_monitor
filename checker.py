from selenium.webdriver.common.by import By
from dictonary import xpath
def check_avalibility(driver):
    avalibility = False
    for paths in xpath:
        if (driver.find_elements_by_xpath(xpath[paths])!=[]):
            avalibility = True
    return avalibility

def check_avalibility_test(driver):
    avalibility = False
    i = 0
    for paths in xpath:
        i = i+1
        print(str(i))
        print(driver.find_elements_by_xpath(xpath[paths]))
        if (driver.find_elements_by_xpath(xpath[paths])!=[]):
            avalibility = True
    return avalibility