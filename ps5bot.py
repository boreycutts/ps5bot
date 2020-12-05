from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random

start_time = time.time()
n = 0

url = input("URL=")
text = input("TEXT=")


while True:
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver_walmart = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/borey/Downloads/chromedriver')

    n += 1
    print("--- This mf been running for %s seconds and %s iterations ---" % (time.time() - start_time, str(n)))

    driver_walmart.get(url)
    time.sleep(10)
    try:
        get_in_stock_button = driver_walmart.find_element_by_xpath("//*[contains(text(), '" + text + "')]")
    except(Exception):
        print("LETS GOOOOOOOOOOOOOOOOOO")
        break
    
    time.sleep(random.randint(5, 10))
    driver_walmart.quit()

driver_walmart.get("https://www.youtube.com/watch?v=QwbpOltPRic&t=1s&ab_channel=BaconAkin")
#        .-""""-.        .-""""-.
#       /        \      /        \
#      /_        _\    /_        _\
#     // \      / \\  // \      / \\
#     |\__\    /__/|  |\__\    /__/|
#      \    ||    /    \    ||    /
#       \        /      \        /
#        \  __  /        \  __  / 
#         '.__.'          '.__.'
#          |  |            |  |
#          |  |            |  |