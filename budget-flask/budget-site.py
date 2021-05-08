from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main')
def main_page():
    return render_template("home.html")

@app.route('/sign-up')
def sign_up_page():
    return "This is the sign up page.."

@app.route('/about')
def about():
    return render_template("about.html")

