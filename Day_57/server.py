from flask import Flask, render_template
import random, datetime, requests
app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    # Adding an import to the HTML file
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    # Get data from API
    # Gender
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    # Age
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)