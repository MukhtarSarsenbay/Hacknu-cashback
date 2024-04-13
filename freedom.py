from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

# Replace the following with your actual database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/template1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the CashbackOffer model
class CashbackOffer(db.Model):
    __tablename__ = 'cashback_offers'

    offerID = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    cashback_percentage = db.Column(db.Float, nullable=False)
    conditions = db.Column(db.String(200), nullable=False)
    validity = db.Column(db.Date, nullable=False, default=datetime.now)
    restrictions = db.Column(db.String(200))

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
        percentage_pattern = r'\b\d+\b'
        element = element.text.strip()
        # Find all percentages in the original string
        percentages = re.findall(percentage_pattern, element)
        cashback_percentage = int(percentages[0])
        # Print the content of the element
        max_offer_id = db.session.query(db.func.max(CashbackOffer.offerID)).scalar() or 0

        if element:
            offer = CashbackOffer(
                offerID=max_offer_id + 1,
                bank_name='Freedom',
                category='Прочие платежи по карточке',
                cashback_percentage=cashback_percentage,
                conditions=element,  # Join percentages as string
                validity=datetime.now(),  # Default to current date
                restrictions=''  # Default to empty string
            )
            db.session.add(offer)

            # Commit the changes to the database
        db.session.commit()


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

