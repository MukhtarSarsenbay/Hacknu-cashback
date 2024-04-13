import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://home.kz/debit-cards/HomeCard-Lite'

# Send a GET request to the webpage
response = requests.get(url, verify=False)
data = response.text

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

print(soup.title.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Use CSS selector to find the desired element
    element = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2) > a')

    # Print the content of the element
    if element:
        print("Content of the element:", element.text.strip())
    else:
        print("Element not found")
else:
    print("Failed to fetch the webpage")