from selenium import webdriver
import time




# options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
)
# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(options=options)

try:
    driver.get("http://useragentstring.com/")
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
