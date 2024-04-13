from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests
app = Flask(__name__)
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
    validity = db.Column(db.Date, nullable=False)
    restrictions = db.Column(db.String(200))


class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    # Relationship to Bank Cards
    bank_cards = db.relationship('BankCard', backref='user', lazy=True)
    # Relationship to Cashback Offers
    cashback_offers = db.relationship('CashbackOffer', backref='user', lazy=True)


class BankCard(db.Model):
    __tablename__ = 'bank_cards'

    cardID = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String, nullable=False)
    card_type = db.Column(db.String, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable=False)

# Function to print the content of the cashback_offers table

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(name=request.form['name'], surname=request.form['surname'],
                        email=request.form['email'], address=request.form['address'],
                        phone=request.form['phone'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.userID
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f'Welcome, user #{session["user_id"]}!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
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


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    db.create_all()
    print_cashback_offers()