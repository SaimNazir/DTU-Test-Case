from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello there"

if __name__ == '__main__':
    # Set host to '0.0.0.0' to allow access from outside the container, and port to 8000 for Azure
    app.run(host='0.0.0.0', port=8000)


