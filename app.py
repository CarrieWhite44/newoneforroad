from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'Title': 'Software Engineer',
    'Location': 'Sydney',
    'Salary': '$6000'
  },
  
  { 
    'id': 2,
    'Title': 'Middle-Python',
    'Location': 'Monreal',
  },
  
  {
    'id': 3,
    'Title': 'Senior-Python',
    'Location': 'Sydney',
    'Salary': '$7000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Carrie')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
