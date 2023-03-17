from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Bengaluru,India",
  "Salary": "Rs 10,00,000"
}, {
  "id": 2,
  "title": "Data Scientist",
  "location": "Delhi,India",
  "Salary": "Rs 15,00,000"
}, {
  "id": 3,
  "title": "Frontend Engineer",
  "location": "Remote",
}, {
  "id": 4,
  "title": "Backend Engineer",
  "location": "San Francisco, USA",
  "Salary": "$ 120,000"
}]


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
