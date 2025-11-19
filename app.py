from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from query import tree_display, collect_info, Person, load_people, convert_json, link_prep
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
people = load_people()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/input_relative', methods=["GET"])
def collect():
    collect_info()
    return render_template("form.html")


@app.route('/load_people', methods=["GET"])
def show_people():
    loaded_people = load_people()
    return loaded_people


@app.route('/convert_json', methods=["GET"])
def organize():
    convert_json()
    return render_template("tree.html")


@app.route('/show_relative', methods=["GET"])
def save_info():
    Person()
    return render_template("form.html")

# double check above on how to implement this

# @app.route('/show_family_tree', methods=["GET"])
# def show_family_tree():
#     tree_display()
#     return render_template("family_tree.html")


# make a python function here and make another route that would call this function, the java script in the html should query the python
# query.py is the main backend part of the entire project, standalone it should hold most of the logic, flask is the intermediary that allows it to be the front end

# query.py --> main meat of the project
# app.py --> get chat GPT to build this, not as important as working on the query.py, this is mostly a config file
# theorydraft./html --> index.html
