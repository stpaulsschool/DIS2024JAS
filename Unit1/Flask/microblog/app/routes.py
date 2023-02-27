from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"Username": "Jeffrey"}
    posts = [
        {
        "Author": {"Username": "Fred"},
        "Body": "Beautiful day in Brisbane!"
        },
        {
        "Author": {"Username": "William"},
        "Body": "Basketball is the best sport!"
        }
    ]
    return render_template("index.html", title=user["Username"], user=user, posts=posts)