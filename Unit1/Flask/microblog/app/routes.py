from app import app
@app.route("/")
def default():
    return "<H1>Hello; Default</H1>"

@app.route("/index")
def index():
    return "<H1>Hello World; Index</H1>"