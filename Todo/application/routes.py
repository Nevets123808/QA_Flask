from application import app, db
from application.models import Tasks
from application.forms import TodoForm
from flask import render_template, request
from datetime import date

@app.route('/')
def home():
    tasks = Tasks.query.filter_by(completed=False).all()
    return render_template("index.html", todo = tasks)

@app.route('/add', methods =['GET', 'POST'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_task = Tasks(name = form.task_name.data, date_added = date.today())
        db.session.add(new_task)
        db.session.commit()
        message = "Task Added! Go back to index to see."
        return render_template("add.html",form=form, message = message)
    else:
        return render_template("add.html", form=form, message = form.task_name.errors)

@app.route('/complete/<ID>')
def complete(ID):
    task = Tasks.query.get(int(ID))
    task.completed = True
    db.session.commit()
    return f"Task {ID} completed!"

@app.route('/incomplete/<ID>')
def incomplete(ID):
    task = Tasks.query.get(int(ID))
    task.completed = False
    db.session.commit()
    return f"Task {ID} marked incomplete!"

@app.route('/update/<TASK>')
def update(TASK):
    task = Tasks.query.order_by(Tasks.date_added.desc()).first()
    task.name = TASK
    db.session.commit()
    return f"Most recent task is now {TASK}"