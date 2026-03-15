from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """Hello,<br>
My name is Shafique.<br>
I have built DNS_Record application"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)