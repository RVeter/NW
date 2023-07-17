import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_i_see_button_add_to_busket(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button) == 1, "Not uniqe locator"