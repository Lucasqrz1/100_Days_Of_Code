from flask import Flask
app = Flask(__name__)

print(__name__)
# A simple page that says hello.
@app.route("/")
def hello():
    return "Hello World!"

# Execute only if run as a script.
if __name__ == "__main__":
    app.run()

# Understanding python decorators, explaining the "Flask(__name__)"
def delayer(func):
    def wrapper():
        print("delaying")
        func()
        print("delayed")
    return wrapper

# The decorator must be placed right above the function it decorates.
@delayer
def say_hi():
    print("hi")
say_hi()

@delayer
def say_bye():
    print("bye")
say_bye()