from application import app, db
from application.models import Tasks
from flask import render_template
from datetime import date

@app.route('/')
def home():
    tasks = Tasks.query.filter_by(completed == False).all()
    return render_template("index.html", todo = tasks)

@app.route('/add')
def add():
    new_task = Tasks(name = "Do something", date_added = date.today())
    db.session.add(new_task)
    db.session.commit()
    return "Add a new Todo"

@app.route('/complete/<ID>')
def complete(ID):
    task = Tasks.query.get(int(ID))
    task.completed = True
    db.session.commit()