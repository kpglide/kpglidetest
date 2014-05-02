from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True, port=8080)