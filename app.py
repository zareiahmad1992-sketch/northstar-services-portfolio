from pathlib import Path
import json
import os

from flask import Flask, render_template, request

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "services.json"

app = Flask(__name__)


def load_services():
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def index():
    services = load_services()
    selected_category = request.args.get("category", "All")
    search_term = request.args.get("q", "").strip()

    if selected_category != "All":
        services = [item for item in services if item["category"] == selected_category]

    if search_term:
        query = search_term.lower()
        services = [
            item for item in services
            if query in item["name"].lower()
            or query in item["description"].lower()
            or query in item["category"].lower()
        ]

    categories = sorted({item["category"] for item in load_services()})
    return render_template(
        "index.html",
        services=services,
        categories=categories,
        selected_category=selected_category,
        search_term=search_term,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
