from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# make a python function here and make another route that would call this function, the java script in the html should query the python
# query.py is the main backend part of the entire project, standalone it should hold most of the logic, flask is the intermediary that allows it to be the front end

# query.py --> main meat of the project
# app.py --> get chat GPT to build this, not as important as working on the query.py, this is mostly a config file
# theorydraft./html --> index.html

