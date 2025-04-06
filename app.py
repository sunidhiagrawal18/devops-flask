from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Yo! I'm alive. Your DevOps pipeline is lit 🚀"

if __name__ == '__main__':
    app.run(debug=True)
