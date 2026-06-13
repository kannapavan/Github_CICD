from flask import Blueprint, jsonify, render_template, session, request, redirect, url_for
from app.config import Config

main_bp = Blueprint("main", __name__)

PRODUCTS = [
    {
        "id": 1, "name": "$25 Virtual Gift Card",
        "description": "$25 Gift Card redeemable toward eligible products.",
        "price": 25.00, "rating_percent": 63,
        "image": "https://via.placeholder.com/125x125/4a90d9/ffffff?text=Gift+Card",
        "category": "gift-cards"
    },
    {
        "id": 2, "name": "14.1-inch Laptop",
        "description": "Unique Asian-influenced imprint wraps the laptop both inside and out",
        "price": 1590.00, "rating_percent": 72,
        "image": "https://via.placeholder.com/125x125/50b86c/ffffff?text=Laptop",
        "category": "notebooks"
    },
    {
        "id": 3, "name": "Build your own cheap computer",
        "description": "Build it your way with affordable components.",
        "price": 800.00, "rating_percent": 59,
        "image": "https://via.placeholder.com/125x125/e74c3c/ffffff?text=PC+Cheap",
        "category": "desktops"
    },
    {
        "id": 4, "name": "Build your own computer",
        "description": "Customize your perfect machine.",
        "price": 1200.00, "rating_percent": 57,
        "image": "https://via.placeholder.com/125x125/f39c12/ffffff?text=PC+Custom",
        "category": "desktops"
    },
    {
        "id": 5, "name": "Build your own expensive computer",
        "description": "Premium components for the ultimate build.",
        "price": 1800.00, "rating_percent": 59,
        "image": "https://via.placeholder.com/125x125/9b59b6/ffffff?text=PC+Pro",
        "category": "desktops"
    },
    {
        "id": 6, "name": "Simple Computer",
        "description": "Affordable and reliable for everyday tasks.",
        "price": 800.00, "rating_percent": 62,
        "image": "https://via.placeholder.com/125x125/1abc9c/ffffff?text=Simple+PC",
        "category": "desktops"
    },
]

@main_bp.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@main_bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@main_bp.route("/version")
def version():
    return jsonify({
        "version": Config.APP_VERSION,
        "environment": Config.ENVIRONMENT
    })

@main_bp.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello {name}!"})

@main_bp.route("/books")
def books():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] in ("books",)])

@main_bp.route("/computers")
def computers():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] in ("desktops", "notebooks", "accessories")])

@main_bp.route("/desktops")
def desktops():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] == "desktops"])

@main_bp.route("/notebooks")
def notebooks():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] == "notebooks"])

@main_bp.route("/electronics")
def electronics():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] in ("camera-photo", "cell-phones")])

@main_bp.route("/apparel-shoes")
def apparel_shoes():
    return render_template("index.html", products=[])

@main_bp.route("/digital-downloads")
def digital_downloads():
    return render_template("index.html", products=[])

@main_bp.route("/jewelry")
def jewelry():
    return render_template("index.html", products=[])

@main_bp.route("/gift-cards")
def gift_cards():
    return render_template("index.html", products=[p for p in PRODUCTS if p["category"] == "gift-cards"])

@main_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return render_template("index.html", products=PRODUCTS)
    return render_template("index.html", products=[product])

@main_bp.route("/search")
def search():
    q = request.args.get("q", "").lower()
    results = [p for p in PRODUCTS if q in p["name"].lower() or q in p["description"].lower()] if q else PRODUCTS
    return render_template("index.html", products=results)

@main_bp.route("/add-to-cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("main.home"))

@main_bp.route("/cart")
def cart():
    cart_products = []
    if "cart" in session:
        for pid in session["cart"]:
            p = next((x for x in PRODUCTS if x["id"] == pid), None)
            if p:
                cart_products.append(p)
    return render_template("index.html", products=cart_products)
