from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            # Get the numbers from the form
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            # Calculate the sum
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    
    # Render the template with the result
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)