# make a Flask bases API to run a page

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file(path)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
