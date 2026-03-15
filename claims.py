from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, my name is Anjali Roy. I have built Claims Management service application."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
