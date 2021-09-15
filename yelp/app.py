from flask import Flask, render_template, request
import os, random
from scraper import scrape

app = Flask(__name__)
random.seed(0)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		business = request.form['business']
		location = request.form['location']
		pages = int(request.form['pages'])
		scrape(business, location, pages)
		return render_template('index.html')
	else:
		return render_template('index.html')	


if __name__ == '__main__':
	app.run(debug=True)


