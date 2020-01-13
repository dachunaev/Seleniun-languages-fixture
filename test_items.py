from selenium.webdriver.common.by import By
import time


def test_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    try:
        browser.get(link)
        assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) == 1, "Basket button not found"
    except():
        pass
