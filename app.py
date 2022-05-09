from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	myH1 = "Week2"
	return render_template("index.html", TheH1 = myH1)

@app.route('/about')
def about():
	names = ["Joe", "Bill", "Wes"]
	return render_template("about.html", names=names)

@app.route('/projects')
def projects():
	title = "Projects List"

	return render_template("projects.html", title=title)