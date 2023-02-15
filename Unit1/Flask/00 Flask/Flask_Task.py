from flask import Flask #We need to import Flask

app = Flask(__name__) #We need to create an instance of this class

@app.route('/') #We the use the route() decorator to tell Flask what URL should trigger our function

def hello_form():
    return "<p>Hello, this is a form!</p>"
    #this function returns the message we want to display in the browser

if __name__ == '__main__':
    app.run(debug=True)