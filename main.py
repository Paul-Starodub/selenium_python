from selenium import webdriver
import time


# url = "https://www.instagram.com/"

#options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Hello World")

driver = webdriver.Chrome(options=options)


try:
    # driver.get(url)
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)

    # driver.refresh()
    # time.sleep(2)

    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
