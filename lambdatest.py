from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')
