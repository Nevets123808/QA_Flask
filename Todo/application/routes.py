from application import app, db
from application.models import Tasks
from application.forms import TodoForm
from flask import render_template, request, redirect, url_for
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
        return redirect(url_for('home'))
    else:
        return render_template("add.html", form=form)

@app.route('/complete/<ID>')
def complete(ID):
    task = Tasks.query.get(int(ID))
    task.completed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/<ID>')
def incomplete(ID):
    task = Tasks.query.get(int(ID))
    task.completed = False
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<ID>', methods = ['GET', 'POST'])
def update(ID):
    form = TodoForm()
    task = Tasks.query.get(ID)
    if form.validate_on_submit():
        task.name = form.task_name.data
        db.session.commit()
        return redirect(url_for('home'))
    else:    
        return render_template('update.html', form = form, task=task)

@app.route('/delete/<ID>')
def delete(ID):
    task_to_delete = Tasks.query.get(int(ID))
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))