from flask import Blueprint, jsonify
from app.config import Config

main_bp = Blueprint("main", __name__)

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
