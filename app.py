from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace the following with your actual database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/template1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# User Model
class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))

    # Relationship to bank cards
    bank_cards = db.relationship('BankCard', backref='owner', lazy=True)


# Bank Card Model
class BankCard(db.Model):
    __tablename__ = 'bank_cards'

    cardID = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    card_type = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(20), nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable=False)


# Cashback Offers Model
class CashbackOffer(db.Model):
    __tablename__ = 'cashback_offers'

    offerID = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    cashback_percentage = db.Column(db.Float, nullable=False)
    conditions = db.Column(db.String(200), nullable=False)
    validity = db.Column(db.Date, nullable=False)
    restrictions = db.Column(db.String(200))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
