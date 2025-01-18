from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! If you can see this, the web server is working!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8515, debug=True)
