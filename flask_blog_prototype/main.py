from flask import Flask, render_template, request
import requests
import smtplib


OWN_EMAIL=""
OWN_PASSWORD=""
url_end_point = " https://api.npoint.io/91997184c10bd8cfb48f"
blog_response = requests.get(url_end_point).json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=blog_response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    return render_template("post.html", posts=blog_response, blog_id=blog_id)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)