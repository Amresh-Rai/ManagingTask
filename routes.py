from flask import render_template, url_for, flash, redirect, request
from app import app, db
from forms import TaskForm
from models import Task
from datetime import datetime
from sqlalchemy import or_

@app.route("/")
def index():
    search_query = request.args.get('search', '')
    if search_query:
        tasks = Task.query.filter(or_(Task.title.contains(search_query), Task.description.contains(search_query))).all()
    else:
        tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, search_query=search_query)

@app.route("/task/new", methods=['GET', 'POST'])
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, 
                    due_date=form.due_date.data, status=form.status.data, remarks=form.remarks.data,
                    created_by_name=form.user_name.data, created_by_id=form.user_id.data,
                    last_updated_by_name=form.user_name.data, last_updated_by_id=form.user_id.data)
        db.session.add(task)
        db.session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('task_form.html', title='New Task', form=form, legend='New Task')

@app.route("/task/<int:task_id>/update", methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.status = form.status.data
        task.remarks = form.remarks.data
        task.last_updated_by_name = form.user_name.data
        task.last_updated_by_id = form.user_id.data
        task.last_updated_on = datetime.utcnow()
        db.session.commit()
        flash('Your task has been updated!', 'success')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
        form.status.data = task.status
        form.remarks.data = task.remarks
        form.user_name.data = task.last_updated_by_name
        form.user_id.data = task.last_updated_by_id
    return render_template('task_form.html', title='Update Task', form=form, legend='Update Task')

@app.route("/task/<int:task_id>/delete", methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Your task has been deleted!', 'success')
    return redirect(url_for('index'))
