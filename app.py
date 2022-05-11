from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
	myH1 = "Projects"
	return render_template("index.html", TheH1 = myH1)

@app.route('/projects')
def projects():
	title = "List Projects"
	names = ["Refurbish", "Fire Suppression", "Water Valves"]
	return render_template("projects.html", names=names)


