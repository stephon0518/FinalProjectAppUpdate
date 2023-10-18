import requests
from bs4 import BeautifulSoup


#Accessing the webpage for the reviews
url = "https://play.google.com/store/apps/details?id=com.instagram.android&hl=en_US&gl=US&pli=1"
response = requests.get(url)

if response.status_code == 200:
    page_content = response.content
else:
    print("Failed to retrieve the web page.")

soup = BeautifulSoup(page_content, 'html.parser')

#Getting the reviews through inspection of the elements
reviews_divs = soup.find_all('div', class_='h3YV2d')

for review_div in reviews_divs:
    # Example extraction of review text
    review_text = review_div.text
    
    with open('reviews_output.txt', 'a', encoding='utf-8') as f:
        f.write(review_text + '\n')