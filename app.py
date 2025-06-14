from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            desired_amount = float(request.form["amount"])
            percent_fee = float(request.form["percent"]) / 100
            fixed_fee = float(request.form["fixed"])

            customer_pays = round((desired_amount + fixed_fee) / (1 - percent_fee), 2)
            result = f"You should charge: AED {customer_pays}"
        except:
            result = "Invalid input. Please try again."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
