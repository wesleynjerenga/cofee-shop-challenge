from flask import Flask, render_template, request, redirect, url_for
from customer import Customer
from coffee import Coffee
from order import Order

app = Flask(__name__, template_folder='templates')

# Sample data
if not Customer._all:
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    Order(alice, espresso, 3.5)
    Order(bob, latte, 4.0)

@app.route("/")
def index():
    customers = Customer._all
    coffees = Coffee._all
    orders = Order._all
    return render_template("index.html", customers=customers, coffees=coffees, orders=orders)

@app.route("/add_order", methods=["POST"])
def add_order():
    customer = Customer._all[int(request.form["customer"])]
    coffee = Coffee._all[int(request.form["coffee"])]
    price = float(request.form["price"])
    Order(customer, coffee, price)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)