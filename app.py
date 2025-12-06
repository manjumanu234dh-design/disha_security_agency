from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quote", methods=["POST"])
def quote():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    # Basic server-side validation
    if not name or not email or not service:
        return "Please fill in name, email, and service.", 400

    confirmation = (
        f"Thank you, {name}. Your request for '{service}' was received. "
        f"We'll contact you at {email}. Details: {message if message else 'N/A'}"
    )
    return confirmation, 200

if __name__ == "__main__":
    app.run(debug=True)