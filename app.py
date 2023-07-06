from flask import Flask, render_template,jsonify,request
from database import load_jobs_from_db,jobDetails,add_application
app = Flask(__name__)

@app.route("/")
def index():
    JOBS = load_jobs_from_db()
    return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def api_jobs():
    jobs = load_jobs_from_db()
    row = [dict(r) for r in jobs]
    return jsonify(row)

@app.route("/jobs/<id>")
def jobDescription(id):
    job = jobDetails(id)
    if 'Job not found' == job:
        return f'{404} Job not found'
    else:
        res = dict(job)
        return render_template('jobPage.html', job=res)
@app.route("/jobs/<id>/<title>", methods=['GET'])
def jobDesc(id,title):
    JOB = {'Job ID':id,'Job Title':title}
    return render_template('application.html',job=JOB)

@app.route("/jobs/applied/<id>", methods=['POST'])
def jobApply(id):
    data = request.form
    add_application(id, data)
    return render_template('applied.html')


if __name__ == '__main__':
    app.run(debug=True)
