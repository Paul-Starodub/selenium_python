from selenium import webdriver
import time


url = "https://www.instagram.com/"
driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(5)
    driver.get(url="https://stackoverflow.com")
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
