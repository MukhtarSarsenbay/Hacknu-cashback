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

            percentage_pattern = r'\b\d+\b'

            cashbacks = []
            # Check if the request was successful
            if response.status_code == 200:
                # Extract the desired information
                card1name = soup.select_one('body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(1) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2').text.strip()
                card1cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(1) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card1cashbackpercent = re.findall(percentage_pattern, card1cashback)
                cashback_percentage1 = int(card1cashbackpercent[0])
                cashbacks.append(cashback_percentage1)

                card2name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(2) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card2cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(2) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card2cashbackpercent = re.findall(percentage_pattern, card2cashback)
                cashback_percentage2 = int(card2cashbackpercent[0])
                cashbacks.append(cashback_percentage2)

                card3name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(3) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card3cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(3) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card3cashbackpercent = re.findall(percentage_pattern, card3cashback)
                cashback_percentage3 = int(card3cashbackpercent[0])
                cashbacks.append(cashback_percentage3)
                condition3 = soup.select_one('body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(3) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(3)').text.strip()
                
                card4name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(4) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card4cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(4) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card4cashbackpercent = re.findall(percentage_pattern, card4cashback)
                cashback_percentage4 = int(card4cashbackpercent[0])
                cashbacks.append(cashback_percentage4)

                card5name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(5) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card5cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(5) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card5cashbackpercent = re.findall(percentage_pattern, card5cashback)
                cashback_percentage5 = int(card5cashbackpercent[0])
                cashbacks.append(cashback_percentage5)

                card6name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(6) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card6cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(6) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card6cashbackpercent = re.findall(percentage_pattern, card6cashback)
                cashback_percentage6 = int(card6cashbackpercent[0])
                cashbacks.append(cashback_percentage6)
                condition6 = soup.select_one('body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(6) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(3) > div > span:nth-child(2)').text.strip() + soup.select_one('body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(6) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(3) > div > span:nth-child(3)').text.strip()

                card7name = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(7) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.product-cards-caraousel-item-title.transition-all.duration-500.text-2xl.font-semibold.mb-4.\<md\:text-sm.\<md\:mb-2").text.strip()
                card7cashback = soup.select_one("body > div.wrapper > div > main > div > section:nth-child(2) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(7) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)").text.strip()
                card7cashbackpercent = re.findall(percentage_pattern, card7cashback)
                cashback_percentage7 = int(card7cashbackpercent[0])
                cashbacks.append(cashback_percentage7)

                card8name = soup.select_one('body > div.wrapper > div > main > div > section:nth-child(3) > div > div.mb-10 > div > h1 > a').text.strip()
                card8cashback = soup.select_one('body > div.wrapper > div > main > div > section:nth-child(3) > div > div.embla.relative.product-cards-caraousel > div.embla__viewport.overflow-hidden.w-full.mb-8 > div > div:nth-child(1) > div > div > div > div.flex.flex-col.justify-between.p-6.flex-3.order-first.\<md\:pt-3.\<md\:pb-\[18px\].\<md\:px-3 > div:nth-child(1) > div.mb-8.\<md\:text-xs > div:nth-child(1) > div > span:nth-child(2)').text.strip()
                card8cashbackpercent = re.findall(percentage_pattern, card8cashback)
                cashback_percentage8 = int(card8cashbackpercent[0])
                cashbacks.append(cashback_percentage8)

                # Get the current maximum offer ID
                max_offer_id = db.session.query(db.func.max(CashbackOffer.offerID)).scalar() or 0



                # Create instances of CashbackOffer and add them to the database session
                if cashback_percentage1 == cashback_percentage2 and cashback_percentage2 == cashback_percentage7:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage1, 
                        conditions= card1name + ", " + card2name + ", " + card7name,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer)

                if cashback_percentage4:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage4, 
                        conditions= card4name,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer)

                if cashback_percentage6:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage6, 
                        conditions= card6name,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=condition6  # Default to empty string
                    )
                    db.session.add(offer)

                if cashback_percentage3:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage3, 
                        conditions= card3name,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=condition3  # Default to empty string
                    )
                    db.session.add(offer)
                
                if cashback_percentage5:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage5, 
                        conditions= card5name,  # Join percentages as string
                        validity=datetime.now(),  # Default to current date
                        restrictions=''  # Default to empty string
                    )
                    db.session.add(offer)

                if cashback_percentage8:
                    offer = CashbackOffer(
                        offerID=max_offer_id + 1,
                        bank_name='HalykBank', 
                        category='Прочие платежи по карточке',
                        cashback_percentage= cashback_percentage8, 
                        conditions= card8name,  # Join percentages as string
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
