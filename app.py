from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
    validity = db.Column(db.Date, nullable=False)
    restrictions = db.Column(db.String(200))

# Function to print the content of the cashback_offers table
def print_cashback_offers():
    with app.app_context():
        offers = CashbackOffer.query.all()
        print("Cashback Offers:")
        for offer in offers:
            print(f"Offer ID: {offer.offerID}")
            print(f"Bank Name: {offer.bank_name}")
            print(f"Category: {offer.category}")
            print(f"Cashback Percentage: {offer.cashback_percentage}")
            print(f"Conditions: {offer.conditions}")
            print(f"Validity: {offer.validity}")
            print(f"Restrictions: {offer.restrictions}")
            print()

if __name__ == '__main__':
    print_cashback_offers()