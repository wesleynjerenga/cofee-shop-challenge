from flask import Flask, render_template, request, redirect, url_for, flash
from customer import Customer
from coffee import Coffee
from order import Order

app = Flask(__name__, template_folder='../templates')
app.secret_key = 'your-secret-key'  # Needed for flash messages

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
    try:
        customer_index = int(request.form.get("customer", ""))
        coffee_index = int(request.form.get("coffee", ""))
        price = float(request.form.get("price", ""))

        if customer_index < 0 or customer_index >= len(Customer._all):
            raise ValueError("Invalid customer selected")
        if coffee_index < 0 or coffee_index >= len(Coffee._all):
            raise ValueError("Invalid coffee selected")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        customer = Customer._all[customer_index]
        coffee = Coffee._all[coffee_index]
        
        Order(customer, coffee, price)
        flash("Order added successfully!")
        return redirect(url_for('index'))

    except ValueError as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)