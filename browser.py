from selenium import webdriver

def open_browser():
    driver = webdriver.Chrome()
    return driver

def to_site(driver,site):
    driver.get(site)

def refresh_page(driver):
    driver.refresh()