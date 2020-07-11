import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from databse import *

app = Flask(__name__, static_url_path='', template_folder="./templates")

who = ""
Employee_sector = ""
Employee_name  = ""
Employee_username = ""
Employee_email = ""
Employee_education = ""
Employee_internship = ""
Employee_por = ""
Employee_projects = ""
Employee_skills = ""
Employee_phone = ""
Employee_password = ""


@app.route('/')
def home():
	return render_template('homePage.html')

@app.route('/about')
def About():
	return render_template('about.html', title='About')

@app.route('/RecommendedJobs')
def RecommendedJobs():
    return render_template('recommendedJobs.html')

@app.route('/addEducation')
def addEducation():
	return render_template('addEducation.html')

@app.route('/addExperience')
def addExperience():
	return render_template('addExperience.html')

@app.route('/AvailableJobs')
def AvailableJobs():
    return render_template('availableJobs.html')

@app.route('/ResumeBuilder')
def ResumeBuilder():
	return render_template('ResumeBuilder.html')




# employer routing started...
@app.route('/EmployerIndex')
def EmployerIndex():
	return render_template('EmployerIndex.html')

@app.route('/createVacancy')
def createVacancy():
	return render_template('createVacancy.html')

@app.route('/appliedPeople')
def appliedPeople():
	return render_template('appliedPeople.html')

@app.route('/EmployeeProfile')
def EmployeeProfile():
	return render_template('EmployeeProfile.html')

@app.route('/EmployerProfile')
def EmployerProfile():
	return render_template('EmployerProfile.html')


@app.route('/FixMeeting')
def FixMeeting():
	return render_template('FixMeeting.html')

@app.route('/takeMeetings')
def takeMeetings():
	return render_template('takeMeetings.html')

@app.route('/startMeetingEmployer')
def startMeetingEmployer():
	return render_template('startMeetingEmployer.html')

@app.route('/startMeeting')
def startMeeting():
	return render_template('startMeeting.html')

@app.route('/EmployeeInterview')
def EmployeeInterview():
	return render_template('EmployeeInterview.html')

@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def SignUp():
	global who
	if (request.method == 'POST'):
		who = request.form.get("select")
		if(who == "Employee" or who == "Employer"):
			return redirect(url_for('OrganizedOrUnorganized'))

	return render_template('SignUp.html')

@app.route('/OrganizedOrUnorganized', methods=['GET', 'POST'])
def OrganizedOrUnorganized():
	global Employee_sector
	if(request.method == 'POST'):
		Employee_sector = request.form.get("select")
		if(Employee_sector == "Organized"):
			return redirect(url_for(who + "Organized"))
		if(Employee_sector == "Unorganized"):
			return redirect(url_for(who + "Unorganized"))

	return render_template('OrganizedOrUnorganized.html')

@app.route('/EmployeeOrganized', methods=['GET', 'POST'])
def EmployeeOrganized():
	global Employee_name, Employee_username, Employee_email, Employee_education, Employee_internship, Employee_por, Employee_projects
	global Employee_skills, Employee_phone, Employee_password
	if (request.method == 'POST'):
		Employee_name = request.form.get('Name')
		Employee_username = request.form.get('Username')
		Employee_email = request.form.get('Email')
		Employee_education = request.form.get('Education')
		Employee_internship = request.form.get('Internship')
		Employee_por = request.form.get('PositionOfResp')
		Employee_projects = request.form.get('Projects')
		Employee_skills = request.form.get('Skills')
		Employee_phone = request.form.get('Phone')
		Employee_password = request.form.get('Password')

		add_Employee()
		return redirect(url_for('index'))

	return render_template('EmployeeOrganized.html')

def add_Employee():
	data = {
		'sector': Employee_sector,
		'Name': Employee_name,
		'Username': Employee_username,
		'Email_id': Employee_email,
		'Education': Employee_education,
		'Internships': Employee_internship,
		'POR': Employee_por,
		'Project': Employee_projects,
		'Skills': Employee_skills,
		'Phone_no': Employee_phone,
		'Password': Employee_password
	}
	Employees_insert_data(data)


@app.route('/EmployeeUnorganized', methods=['GET', 'POST'])
def EmployeeUnorganized():
	if request.method =='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		EMAIL_ID = request.form.get('Email')
		EXPERIENCE = request.form.get('Experience')
		SKILLS = request.form.get('Skills')
		PHONE_NO = request.form.get('Phone')
		PASSWORD = request.form.get('Password')
		return redirect(url_for('index'))

	return render_template('EmployeeUnorganized.html')

# created a very basic database.
database = {'hello@gmail.com':'123'}
# start fetching the details.
@app.route('/login', methods=['POST', 'GET'])
def login():
	global naam
	if (request.method == 'POST'):
		naam = "waris"
		Email = request.form.get("email")
		Password = request.form.get("pass")

		if Email not in database:
			return render_template('login.html', info='Invalid User')
		else:
			if database[Email] != Password:
				return render_template('login.html', info='Invalid Password')
			else:
				return redirect(url_for('index'))

	return render_template('login.html')


@app.route('/Employer', methods=['POST', 'GET'])
def Employer():
	if request.method=='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		PASSWORD = request.form.get('Password')
		COMPANY_NAME = request.form.get('CompName')
		COMPANY_SIZE = request.form.get('CompSize')
		EMAIL_ID = request.form.get('Email')
		POSITION = request.form.get('Position')
		SECTOR_TYPE = request.form.get('sectorType')
		SECTORNAME = request.form.get('SectName')
		PHONE = request.form.get('Phone')

	return render_template('Employer.html')

@app.route('/contactUs', methods=['POST', 'GET'])
def Contact():
	select="select * from CONTACTUS"
	cur = conn.cursor()
	cur.execute(select)
	row = cur.fetchall()
	if request.method=='POST':
		"""Add entry to the database here"""
		YourName = request.form.get('name')
		YourEmail = request.form.get('email')
		Subject = request.form.get('subject')
		Message = request.form.get('message')

		insert = "insert into CONTACTUS values(?,?,?,?)"
		params = (YourEmail, YourName, Subject, Message)
		stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
		ibm_db.execute(stmt_insert,params)

	return render_template('contactUs.html')

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)