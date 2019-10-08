from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello():
	return "Hello Patrick"

if __name__ == '__main__':
	app.run(debug=True)