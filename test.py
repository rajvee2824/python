import time

from selenium1 import webdriver


# Optional argument, if not specified will search path.
driver = webdriver.Chrome('/path/to/chromedriver')

driver.get('https://dev.artistongo.com/')

time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()
