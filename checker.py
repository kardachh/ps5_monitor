from selenium.webdriver.common.by import By

def check_avalibility(driver):
    a = str(driver.find_element_by_class_name("add-to-basket-button"))
    #c-btn c-btn_text o-pay__btn sel-pdp-button-place-to-cart sel-button-place-to-cart sel-product-tile-button-to-cart')
    return a