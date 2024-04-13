import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://berekebank.kz/ru/personal/cards/allin'

# Send a GET request to the webpage
response = requests.get(url)
data = response.text

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page with BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Use a lambda function to safely check for 'cashback' in elements' text
#     cashback_elements = soup.find_all(['p', 'div', 'span'], text=lambda t: t and 'cashback' in t.lower())


soup = BeautifulSoup(data, "html.parser")
print(soup.title)
movies = [movie.getText() for movie in soup.find_all(name="ul", class_="feature__list")]
movies = movies[::-1]
print(movies)