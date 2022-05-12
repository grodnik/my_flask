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

@app.route('/addproject')
def addproject():
	title = "Add Project"
	return render_template("addproject.html", title=title)

@app.route('/dispproject', methods=["POST"])
def dispproject():
	title = "Display Project"

	prj_title = request.form.get("prj_title")
	est_start = request.form.get("est_start")
	est_cost = request.form.get("est_cost")

	if not prj_title or not est_start or not est_cost:
		error_message = "All fields required"
		return render_template("addproject.html", error_message=error_message,
				title=title, 
				prj_title=prj_title,  
				est_start = est_start, 
				est_cost=est_cost)

	return render_template("dispproject.html", 
		title=title, prj_title=prj_title,  
		est_start = est_start, est_cost=est_cost )


