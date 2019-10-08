from flask import Flask

app = Flask("Hello World")


@app.route('/hello')
def hello(name="Welt"):
	print("Hallo " + name + "!")

hello(name="Patrick")

hello()


if __name__ == "__main__":
    app.run(debug=True, port=5000)


