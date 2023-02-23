from app import app
@app.route("/")
@app.route("/index")
def index():
    return "<H1>Hello World</H1>"