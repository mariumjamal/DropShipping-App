from flask import Flask, render_template, request
from inventory import get_current_inventory
from waitress import serve

app = Flask(__name__) #makes our app a flask app

@app.route('/') #routes that we will access on web
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/inventory')
def get_inventory():
    item = request.args.get('item')
    inventory_response = get_current_inventory(item)

     # Create a list to store the extracted data
    extracted_data = []

    items = inventory_response.get("result", {}).get("resultList", [])
    # Extract specific fields you want
    for item in items:
        product = item.get("item", {})
        itemTitle = product.get("title", "No title")
        itemQuantity = product.get("sales", "Not available")
        itemPrice = product.get("sku", {}).get("def", {}).get("promotionPrice", "No price")
        print(f"Product: {itemTitle}, Quantity: {itemQuantity}, Price: {itemPrice}")

        # Add the extracted information to the list
        if itemQuantity > 0 :
            extracted_data.append({
            "Title": itemTitle,
            "QuantityAvailable": itemQuantity,
            "Price": itemPrice,
        })


    return render_template("inventory.html", products=extracted_data)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000)