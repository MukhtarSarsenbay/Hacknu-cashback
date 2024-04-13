import requests
from bs4 import BeautifulSoup
from lxml import etree

choice = input()
Cards = ['Deposit CARD', 'Карта Freepay','Премиальная Freedom card', 'Карта инвестора Prestige', 'Премиальная Deposit card']
if choice == Cards[0]:
    # URL of the page to scrape
    #Deposit CARD
    url = 'https://bankffin.kz/ru/card-issuance/deposit-card'

    # Send a GET request to the webpage
    response = requests.get(url, verify=False)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        # Use CSS selector to find the desired element
        element = soup.select_one('body > div.deposit-card.main-wrapper > section:nth-child(3) > div > div.benefits-list.row > div:nth-child(4) > div > p.benefit-title')

        # Print the content of the element
        if element:
            print("Content of the element:", element.text.strip())
        else:
            print("Element not found")
    else:
        print("Failed to fetch the webpage")

if choice == Cards[1]:
    #Карта Freepay:

    url = 'https://bankffin.kz/ru/card-issuance/freepay-card'

    # Send a GET request to the webpage
    response = requests.get(url, verify=False)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        # Use CSS selector to find the desired element
        element = soup.select_one('body > div.freePay-card.main-wrapper > section.freePay-info > div.container > div.benefits > div:nth-child(3) > p')

        # Print the content of the element
        if element:
            print("Content of the element:", element.text.strip())
        else:
            print("Element not found")
    else:
        print("Failed to fetch the webpage")

if choice == Cards[2]:
    #Премиальная Freedom card
    url = 'https://bankffin.kz/ru/cards/premium/freedom-card'

    # Send a GET request to the webpage
    response = requests.get(url, verify=False)
    data = response.text
    print(data)
    soup = BeautifulSoup(data, 'html.parser')



    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use CSS selector to find the desired element
        element = soup.find('td', text=lambda text: text and "%" in text)

        # Print the content of the element
        if element:
            print("Content of the element:", element.text.strip())
        else:
            print("Element not found")
    else:
        print("Failed to fetch the webpage")


if choice == Cards[3]:
    # Карта инвестора Prestige

    url = 'https://bankffin.kz/ru/cards/premium/prestige-card'

    # Send a GET request to the webpage
    response = requests.get(url, verify=False)
    data = response.text
    print(data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use CSS selector to find the desired element
        element = soup.find('td', text=lambda text: text and "%" in text)

        # Print the content of the element
        if element:
            print("Content of the element:", element.text.strip())
        else:
            print("Element not found")
    else:
        print("Failed to fetch the webpage")


if choice == Cards[4]:
    #Премиальная Deposit card

    url = 'https://bankffin.kz/ru/cards/premium/deposit-card'

    # Send a GET request to the webpage
    response = requests.get(url, verify=False)
    data = response.text
    print(data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use CSS selector to find the desired element
        element = soup.find('td', text=lambda text: text and "%" in text)

        # Print the content of the element
        if element:
            print("Content of the element:", element.text.strip())
        else:
            print("Element not found")
    else:
        print("Failed to fetch the webpage")