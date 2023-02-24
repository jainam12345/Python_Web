from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{
  "index": "1",
  "title": "Computer Engineer",
  "Salary": "$100,000",
  "location": "Kampala, Uganda"
}, {
  "index": "2",
  "title": "Backend Engineer",
  "Salary": "$120,000",
  "location": "California, USA"
}, {
  "index": "3",
  "title": "Front-End Developer",
  "Salary": "$90,000",
  "location": "Remote"
}, {
  "index": "4",
  "title": "Data Analyst",
  "Salary": "$140,000",
  "location": "Ahmedabad, India"
}]


@app.route("/")
def hello():
  return render_template('index.html', jobs=JOBS)

@app.route("/jobs")
def jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
