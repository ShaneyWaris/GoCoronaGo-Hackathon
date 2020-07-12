from flask import Flask, render_template, request, url_for, redirect
from Employees_databse import *
from Employer_database import *
import os

# Flask app.
app = Flask(__name__)
port = int(os.getenv('PORT', 8000))
# User is Employee or Employer is stored in "who" variable.
who = ""

# Employee Sector is 'Organized' or 'Unorganized'.
Employee_sector = ""

# Employee Common Variables.
Employee_name  = ""
Employee_username = ""
Employee_email = ""
Employee_skills = ""
Employee_phone = ""
Employee_password = ""

# Employee Organized Variables.
Employee_education = ""
Employee_internship = ""
Employee_por = ""
Employee_projects = ""

# Employee Unorganized Variables.
Employee_experience = ""

#Employer Variables.
Employer_name = ""
Employer_username = ""
Employer_email = ""
Employer_sector = ""
Employer_sector_name = ""
Employer_company_name = ""
Employer_position = ""
Employer_company_size = ""
Employer_phone = ""
Employer_website = ""
Employer_password = ""


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
		if(who == "Employee"):
			return redirect(url_for('OrganizedOrUnorganized'))
		if(who == "Employer"):
			return redirect(url_for('Employer'))

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

		add_Employee_Organized()
		return redirect(url_for('login'))

	return render_template('EmployeeOrganized.html')

@app.route('/EmployeeUnorganized', methods=['GET', 'POST'])
def EmployeeUnorganized():
	global Employee_name, Employee_username, Employee_email, Employee_experience, Employee_skills, Employee_phone, Employee_password
	if (request.method =='POST'):
		Employee_name = request.form.get('Name')
		Employee_username = request.form.get('Username')

		Employee_email = request.form.get('Email')
		Employee_experience = request.form.get('Experience')

		Employee_skills = request.form.get('Skills')
		Employee_phone = request.form.get('Phone')
		Employee_password = request.form.get('Password')

		add_Employee_Unorganized()
		return redirect(url_for('login'))

	return render_template('EmployeeUnorganized.html')


@app.route('/Employer', methods=['POST', 'GET'])
def Employer():
	global Employer_name, Employer_username, Employer_email, Employer_sector, Employer_sector_name, Employer_company_name, Employer_position
	global Employer_company_size, Employer_phone, Employer_website, Employer_password
	if (request.method == 'POST'):
		Employer_name = request.form.get('Name')
		Employer_username = request.form.get('Username')
		Employer_password = request.form.get('Password')
		Employer_company_name = request.form.get('CompanyName')

		Employer_company_size = request.form.get('CompanySize')
		Employer_email = request.form.get('Email')
		Employer_position = request.form.get('Position')
		Employer_sector = request.form.get('select')

		Employer_sector_name = request.form.get('SectorName')
		Employer_phone = request.form.get('Phone')
		Employer_website = request.form.get('Website')

		add_Employer()
		return redirect(url_for('login'))

	return render_template('Employer.html')

def add_Employer():
    data = {
		'Sector': Employer_sector,
		'Name': Employer_name,
    	'Username': Employer_username,
	    'Password': Employer_password,
	    'Company_Name': Employer_company_name,
	    'Company_Size': Employer_company_size,
	    'Email': Employer_email,
	    'Position': Employer_position,
		'Sector_name': Employer_sector_name,
	    'Phone_no': Employer_phone,
	    'Website': Employer_website
	}
    Employers_insert_data(data)


def add_Employee_Organized():
	data = {
		'Sector': Employee_sector,
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

def add_Employee_Unorganized():
	data = {
		'Sector': Employee_sector,
		'Name': Employee_name,
		'Username': Employee_username,
		'Email_id': Employee_email,
		'Experience':Employee_experience,
		'Skills': Employee_skills,
		'Phone_no': Employee_phone,
		'Password': Employee_password
	}
	Employees_insert_data(data)


@app.route('/login', methods=['POST', 'GET'])
def login():
	if (request.method == 'POST'):
		Email = request.form.get('email')
		Password = request.form.get('password')
		print("**********")
		result, current_user = Authentication(Email, Password)
		if(result):
			return render_template('index.html', user = current_user)
		if (not result and current_user == "Invalid Email"):
			print("Invalid Email Id")
			return render_template('login.html')
		if(not result and current_user == "Invalid Pasword"):
			print("Invalid Password")
			return render_template('login.html')

	return render_template('login.html')


@app.route('/contactUs', methods=['POST', 'GET'])
def Contact():
	if (request.method == 'POST'):
		"""Add entry to the database here"""
		YourName = request.form.get('name')
		YourEmail = request.form.get('email')
		Subject = request.form.get('subject')
		Message = request.form.get('message')

	return render_template('contactUs.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)