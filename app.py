from flask import Flask, jsonify,render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Los Angeles, USA',
    'salary':'$130,000',
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'San Francisco, USA',
    'salary':'$150,000',
  },
  {
    'id':3,
    'title':'Software Engineer',
    'location':'Remote',
    'salary':'$120,000',
  },
]

@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def data():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
