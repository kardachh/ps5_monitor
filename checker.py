from selenium.webdriver.common.by import By
from dictonary import xpath
def check_avalibility(driver):
    avalibility = False
    i = 0
    for paths in xpath:
        i = i+1
        print(str(i)+"\n"+str(driver.find_elements_by_xpath(paths))+"\n")
        if (driver.find_elements_by_xpath(xpath[paths])!=[]):
            avalibility = True
            
    #avalibility = driver.find_elements_by_xpath(xpath[])
    return avalibility
    

# xpath
# /html/body/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div[1]/input
# /html/body/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input