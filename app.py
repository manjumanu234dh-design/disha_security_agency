from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Define routes for each page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)