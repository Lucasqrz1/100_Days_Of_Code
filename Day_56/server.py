from flask import Flask
from flask import render_template

app = Flask(__name__)

# Website homepage
@app.route("/")
def home():
    print("Hello World!")
    # Render HTML template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)