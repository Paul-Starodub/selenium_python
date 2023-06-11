from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
)

driver = webdriver.Chrome(options=options)

try:
    driver.get(
        url="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com"
    )
    time.sleep(1)

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("amoral@gmail.com")
    time.sleep(1)

    password_input = driver.find_element(
        By.CSS_SELECTOR, "input#current-password"
    )
    password_input.clear()
    password_input.send_keys("bbbb789R")
    password_input.send_keys(Keys.ENTER)
    time.sleep(6)



    # login_button = driver.find_element(
    #     By.CSS_SELECTOR, ".LoginModal_cta_bottom_box_button_login__5Fbwv"
    # ).click()
    # time.sleep(7)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
