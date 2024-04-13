from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Replace the following with your actual database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Botik8700@localhost:5433/cashback'
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

def scrape_and_save():
    with app.app_context():
        # URL of the page to scrape
        url = 'https://home.kz/debit-cards/HomeCard-Lite'

        try:
            # Send a GET request to the webpage
            response = requests.get(url, verify=False)
            data = response.text

            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(data, 'html.parser')

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the desired information
                category1 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(1) > a')
                cashback12 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(3)')
                cashback11 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2) > a')
                
                condition1 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > strong')
                condition2 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(3) > strong')

                category2 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(1)')
                cashback21 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(2)')
                cashback22 = soup.select_one('#app > div:nth-child(2) > section:nth-child(6) > div > div > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(3)')

                # Get the current maximum offer ID
                max_offer_id = db.session.query(db.func.max(CashbackOffer.offerID)).scalar() or 0

                # Create instances of CashbackOffer and add them to the database session
                if cashback11 and cashback12:
                    offer1 = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HomeBank', 
                        category=category1.text.strip(),
                        cashback_percentage=float(cashback11.text.strip().strip('%')), 
                        conditions=condition1.text.strip(),
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer1)

                    offer2 = CashbackOffer(
                        offerID=max_offer_id + 2,
                        bank_name='HomeBank', 
                        category=category1.text.strip(),
                        cashback_percentage=float(cashback12.text.strip().strip('%')), 
                        conditions=condition2.text.strip(),
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer2)

                if cashback21 and cashback22 and cashback21.text.strip() == cashback22.text.strip():
                    offer3 = CashbackOffer(
                        offerID=max_offer_id + 3,
                        bank_name='HomeBank', 
                        category=category2.text.strip(),
                        cashback_percentage=float(cashback21.text.strip().strip('%')), 
                        conditions='',
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer3)
                
                elif cashback21 and cashback22 and cashback21.text.strip() != cashback22.text.strip():
                    offer3 = CashbackOffer(
                        offerID=max_offer_id + 3,
                        bank_name='HomeBank', 
                        category=category2.text.strip(),
                        cashback_percentage=float(cashback21.text.strip().strip('%')), 
                        conditions=condition1.text.strip(),
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer3)

                    offer4 = CashbackOffer(
                        offerID=max_offer_id + 4,
                        bank_name='HomeBank', 
                        category=category2.text.strip(),
                        cashback_percentage=float(cashback22.text.strip().strip('%')), 
                        conditions=condition2.text.strip(),
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer4)

                # Commit the changes to the database
                db.session.commit()

                print("Data successfully saved to the database.")
            else:
                print("Failed to fetch the webpage.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    scrape_and_save()
