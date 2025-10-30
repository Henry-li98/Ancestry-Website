from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from query import tree_display, collect_info, Person
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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


# double check above on how to implement this

@app.route('/tree', methods=["GET"])
def tree():
    generation_tree = tree_display()
    return generation_tree


@app.route("/", methods=["GET"])
def root_ok():
    return "OK", 200


@app.route('/collect', methods=["GET"])
def collect():
    data = collect_info()
    return data


@app.route('/person', methods=["GET"])
def ancestor():
    person_info = Person()
    return person_info
# make a python function here and make another route that would call this function, the java script in the html should query the python
# query.py is the main backend part of the entire project, standalone it should hold most of the logic, flask is the intermediary that allows it to be the front end

# query.py --> main meat of the project
# app.py --> get chat GPT to build this, not as important as working on the query.py, this is mostly a config file
# theorydraft./html --> index.html
