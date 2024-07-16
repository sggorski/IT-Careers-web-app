from flask import Flask, jsonify,render_template
from database import get_data, load_job
app = Flask(__name__)

@app.route("/")
def hello():
  JOBS = get_data()
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def data():
  return jsonify(get_data())

@app.route("/job/<id>")
def print_job(id):
  job = load_job(id)
  if not job:
    return "Not found!", 404
  return render_template('job_app.html', job=job)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
