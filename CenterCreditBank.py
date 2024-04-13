from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

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
        url = 'https://www.bcc.kz/personal/cards/kartakarta/'

        try:
            # Send a GET request to the webpage
            response = requests.get(url, verify=False)
            data = response.text

            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(data, 'html.parser')

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the desired information
                cashback_info = soup.select_one('#advantages-image-3 > div.base-section-inner > div > div:nth-child(4) > div > div > div.advantage-card-content > div.advantage-card-desc.typography-content > div').text.strip()
                # Regular expression pattern to find the percentage
                percentage_pattern = r'\b\d+\b'

                # Find all percentages in the original string
                percentages = re.findall(percentage_pattern, cashback_info)
                cashback_percentage = int(percentages[0])

                # Get the current maximum offer ID
                max_offer_id = db.session.query(db.func.max(CashbackOffer.offerID)).scalar() or 0

                # Create instances of CashbackOffer and add them to the database session
                if cashback_percentage:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='CenterCreditBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage, 
                        conditions= cashback_info,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer)

                # Commit the changes to the database
                db.session.commit()

                print("Data successfully saved to the database.")
            else:
                print("Failed to fetch the webpage.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    scrape_and_save()
