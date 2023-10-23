from flask import Flask, render_template

app = Flask(__name__)


# Home page
@app.route('/')
def home():
    # File must be in templates folder
    return render_template("home.html")


@app.route('/about/')
def about():
    return "Website content goes here"


if __name__ == "__main__":
    app.run(debug=True)
