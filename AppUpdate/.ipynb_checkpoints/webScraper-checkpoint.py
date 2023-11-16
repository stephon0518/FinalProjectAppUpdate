# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.edge.service import Service
# from bs4 import BeautifulSoup
# import time

# # Path to the Edge WebDriver
# edge_driver_path = 'C:\\Users\\15135\\msedgedriver.exe'

# # Setup Edge options
# options = webdriver.EdgeOptions()
# options.use_chromium = True
# # If you want the browser window to be headless (invisible)
# # options.add_argument('--headless')

# # Initialize Edge WebDriver with the new Service class
# service = Service(edge_driver_path)
# driver = webdriver.Edge(service=service, options=options)

# # Instagram's Google Play URL
# url = "https://play.google.com/store/apps/details?id=com.instagram.android&hl=en_US&gl=US"
# driver.get(url)

# # Scroll to load reviews
# for _ in range(10):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     time.sleep(2)  # Wait for the page to load

# page_content = driver.page_source
# soup = BeautifulSoup(page_content, 'html.parser')

# reviews_divs = soup.find_all('div', class_='h3YV2d')

# with open('reviews_output.txt', 'a', encoding='utf-8') as f:
#     for review_div in reviews_divs:
#         review_text = review_div.text
#         f.write(review_text + '\n')
#         print('\n' + '\n' + '\n')

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import time

# Path to the Edge WebDriver
edge_driver_path = 'C:\\Users\\15135\\msedgedriver.exe'

# Setup Edge options
options = webdriver.EdgeOptions()
options.use_chromium = True
# If you want the browser window to be headless (invisible)
# options.add_argument('--headless')

# Initialize Edge WebDriver with the new Service class
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

# Instagram's Google Play URL
url = "https://play.google.com/store/apps/details?id=com.instagram.android&hl=en_US&gl=US"
driver.get(url)

# Wait for the page to load and the button to become clickable
time.sleep(5)  # Adjust the sleep time as necessary

# Click the "See all reviews" button
# You may need to adjust the class name based on the actual page structure
see_all_reviews_button = driver.find_element(By.CLASS_NAME, 'VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF')
see_all_reviews_button.click()

# Now that the button has been clicked, you may need to wait for the reviews to load
time.sleep(5)  # Adjust the sleep time as necessary

page_content = driver.page_source
soup = BeautifulSoup(page_content, 'html.parser')

reviews_divs = soup.find_all('div', class_='h3YV2d')

with open('reviews_output.txt', 'a', encoding='utf-8') as f:
    for review_div in reviews_divs:
        review_text = review_div.text
        f.write(review_text + '\n')

driver.quit()

