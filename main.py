from selenium import webdriver
import time
import random
from fake_useragent import UserAgent


# url = "https://www.instagram.com/"

user_agents_lists = ["hello_world", "best_of_the_best", "python_today"]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Hello World")
# options.add_argument(f"user-agent={random.choice(user_agents_lists)}")
# options.add_argument(f"user-agent={useragent.ie}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
options.add_argument("--proxy-server=212.237.16.60:3128")  # use own proxy

driver = webdriver.Chrome(options=options)


try:
    # driver.get(url)
    # driver.get(
    #     url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
    # )
    # time.sleep(5)

    # driver.refresh()
    # time.sleep(2)

    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    driver.get(url="https://ipinfo.io/")
    time.sleep(10)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
