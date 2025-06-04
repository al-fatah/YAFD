from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from local files

orders = []
order_counter = 1

@app.route("/")
def home():
    return "Welcome to YAFD – Yet Another Food Delivery!"

@app.route("/order", methods=["POST"])
def place_order():
    global order_counter
    item = request.form.get("item")
    consumer = request.form.get("consumer")
    if not item or not consumer:
        return "Missing item or consumer name", 400

    order = {
        "id": order_counter,
        "item": item,
        "consumer": consumer,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "Pending"
    }
    orders.append(order)
    order_counter += 1
    return f"Order received from {consumer} for: {item}"

@app.route("/orders", methods=["GET"])
def view_orders():
    return jsonify(orders)

@app.route("/update_status", methods=["POST"])
def update_status():
    try:
        order_id = int(request.form.get("order_id"))
        new_status = request.form.get("status")
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            return jsonify({"message": "Status updated", "order": order})

    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
