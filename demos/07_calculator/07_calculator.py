
from flask import render_template
from flask import Flask



app = Flask("calculator")


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)