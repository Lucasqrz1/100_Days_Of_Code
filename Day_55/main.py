from flask import Flask
app = Flask(__name__)

print(__name__)

# This type of decorator adds features to a given page
@app.route("/")
def hello_world():
    # Adding inline CSS
    return ('<h1 style="text-align: center">Hello World!</h1>' 
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="cat">')

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/bye")
@make_bold
@make_emphasys
@make_underlined
def bye():
    return "Bye!"
# Adding a variable that'll be automatically rendered to the webpage

if __name__ == "__main__":
    # Activate debugger mode
    app.run(debug=True)


