from flask import Flask, render_template_string, request, redirect, url_for
from customer import Customer
from coffee import Coffee
from order import Order

app = Flask(__name__)

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
    return render_template_string("""
    <h1>Coffee Shop Orders</h1>
    <h2>Orders</h2>
    <ul>
    {% for order in orders %}
      <li>{{ order.customer.name }} ordered {{ order.coffee.name }} for ${{ order.price }}</li>
    {% endfor %}
    </ul>
    <h2>Add Order</h2>
    <form method="post" action="{{ url_for('add_order') }}">
      Customer:
      <select name="customer">
        {% for customer in customers %}
          <option value="{{ loop.index0 }}">{{ customer.name }}</option>
        {% endfor %}
      </select>
      Coffee:
      <select name="coffee">
        {% for coffee in coffees %}
          <option value="{{ loop.index0 }}">{{ coffee.name }}</option>
        {% endfor %}
      </select>
      Price: <input type="number" step="0.01" name="price" min="1" max="10" required>
      <input type="submit" value="Add Order">
    </form>
    """, customers=customers, coffees=coffees, orders=orders)

@app.route("/add_order", methods=["POST"])
def add_order():
    customer = Customer._all[int(request.form["customer"])]
    coffee = Coffee._all[int(request.form["coffee"])]
    price = float(request.form["price"])
    Order(customer, coffee, price)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)