from app import app

#@app.route("/")
#def default():
#    return "<H1>Hello; Default</H1>"

@app.route("/")
@app.route("/index")
def index():
    user = {"Username": "Eevee"}
    return '''
<html>
    <head>
        <title>Homepage - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user["Username"] + '''!</h1>
    </body>
</html>'''