from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded student data
students = {
    "4E0BF603": "Suraj Katkar",
    "710A4D08": "Rehan Mamidwar",
    "F6D2D903": "Kabir Alhat",
    "1433302B": "Aditya Bansal",

    # Take the rfids from the card and add them here
}

latest_name = "Waiting for Scan..."
latest_uid = ""

@app.route("/")
def home():
    return render_template(
        "index.html",
        name=latest_name,
        uid=latest_uid
    )w

@app.route("/scan", methods=["POST"])
def scan():

    global latest_name
    global latest_uid

    data = request.get_json()

    uid = data["uid"].upper()

    latest_uid = uid

    latest_name = students.get(uid, "Unknown Student")

    return {
        "status": "success",
        "student": latest_name
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)