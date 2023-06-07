from flask import Flask, render_template

app = Flask(__name__)


# JOB opening
JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'description': 'We are looking for a software engineer to join our team',
        'location': 'Bangalore',
        'salary': '10LPA',
        'job_type': 'Full Time',

    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'description': 'We are looking for a data engineer to join our team',
        'location': 'Pune',
        'salary': '15LPA',
        'job_type': 'Full Time',
        },
    {
        'id': 3,
        'title': 'Data Scientist',
        'description': 'We are looking for a data scientist to join our team',
        'location': 'Mumbai',
        'salary': '20LPA',
        'job_type': 'Full Time',

    },
    {
        'id': 4,
        'title': 'Frontend Engineer Intern',
        'description': 'We are looking for a frontend engineer to join our team',
        'location': 'Delhi',
        'salary': '10LPA',
        'job_type': 'Internship',
    },
    {
        'id': 5,
        'title': 'Backend Engineer Intern',
        'description': 'We are looking for a backend engineer to join our team',
        'location': 'Remote',
        'salary': '15LPA',
        'job_type': 'Internship',
    },
    {
        'id': 6,
        'title': 'Fullstack Engineer Intern',
        'description': 'We are looking for a fullstack engineer to join our team',
        'location': 'Remote',
        'salary': '20LPA',
        'job_type': 'Internship',
    },
    {
        'id': 7,
        'title': 'Devops Engineer',
        'description': 'We are looking for a devops engineer to join our team',
        'location': 'Bangalore',
        'salary': '10LPA',
        'job_type': 'Full Time',
    },
    {
        'id': 8,
        'title': 'Cloud Engineer',
        'description': 'We are looking for a cloud engineer to join our team',
        'location': 'Pune',
        'salary': '15LPA',
        'job_type': 'Internship',
    },
    {
        'id': 9,
        'title': 'Machine Learning Engineer',
        'description': 'We are looking for a machine learning engineer to join our team',
        'location': 'Mumbai',
        'salary': '20LPA',
        'job_type': 'Full Time',
    },
    {
        'id': 10,
        'title': 'Data Analyst Intern',
        'description': 'We are looking for a data analyst to join our team',
        'location': 'Delhi',
        'salary': '10LPA',
        'job_type': 'Internship',
    },

]
@app.route("/")
def index():
    return render_template('index.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(debug=True)
