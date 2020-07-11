import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from databse import *

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
	return render_template('homePage.html')

@app.route('/about')
def About():
	return render_template('about.html', title='About')

@app.route('/index')
def index():
    return render_template('index.html')

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

database = {'hello':'123'}
# start fetching the details.
@app.route('/login', methods=['POST', 'GET'])
def login():
	name = "waris"
	# error = "Kuch Nhi........"
	# if request.method=="POST":
	# 	Username = request.form.get("username")
	# 	Password = request.form.get("password")
	# 	print("******************************************************")
	# 	print("******* Username = ", Username)
	# 	print("******* Password = ", Password)
	# 	print("******************************************************")
	# 	if Username == "admin":
	# 		error = "Welcome hoo!!"
	# 	else:
	# 		error = "username nhi match hua!! :("
	# 	if Username not in database:
	# 		return render_template('login.html', info='Invalid User')
	# 	else:
	# 		if database[Username] != Password:
	# 			return render_template('login.html', info='Invalid Password')
	# 		else:
	# 			return render_template('index.html', name = Username)

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


@app.route('/signup')
def SignUp():
    return render_template('SignUp.html')

@app.route('/sectorType')
def OrganizedOrUnorganized():
    return render_template('OrganizedOrUnorganized.html')


@app.route('/EmployeeOrganized')
def EmployeeOrganized():
	if request.method=='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		EMAIL_ID = request.form.get('Email')
		EDUCATION = request.form.get('Education')
		INTERNSHIP = request.form.get('Internship')
		POSOFRESP = request.form.get('PositionOfResp')
		PROJECTS = request.form.get('Projects')
		SKILLS = request.form.get('Skills')
		PHONENO = request.form.get('Phone')
		PASSWORD = request.form.get('Email')

	return render_template('EmployeeOrganized.html')

@app.route('/EmployeeUnorganized')
def EmployeeUnorganized():
	if request.method =='POST':
		NAME = request.form.get('Name')
		USERNAME = request.form.get('Username')
		EMAIL_ID = request.form.get('Email')
		EXPERIENCE = request.form.get('Experience')
		SKILLS = request.form.get('Skills')
		PHONE_NO = request.form.get('Phone')
		PASSWORD = request.form.get('Password')

	return render_template('EmployeeUnorganized.html')

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)