#encoding:utf8
import flask
from flask import request,redirect,flash,render_template,url_for
from todolist.exts import db
from todolist.models import Todo

todo_bp = flask.Blueprint(
    'todo',
    __name__,
    template_folder='../templates'     #创建一个蓝图
)

@todo_bp.route('/',methods = ['GET','POST'])
def index():
    todo = Todo.query.order_by('id')    #两个方法，如果是post，那么就添加数据，否则就是请求数据。
    _form = request.form
    if request.method == 'POST':
        title = _form['title']
        td = Todo(title = title)
        try:
            td.store_to_db()
            flash('add task Done')
            return  redirect(url_for('todo.index'))
        except Exception as e:
            print e
            flash('add failue')
    return render_template('index.html',todo = todo)

@todo_bp.route('/<int:todo_id>/del')
def del_todo(todo_id):
    # todo = Todo.query.filter(Todo.id == todo_id).first()
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        todo.delete_todo()
    flash('deleted task')
    return redirect(url_for('todo.index'))

@todo_bp.route('/<int:todo_id>/edit',methods = ['GET','POST'])
def edit(todo_id):
    todo = Todo.query.filter(Todo.id == todo_id).first()
    if request.method == 'POST':
        Todo.query.filter(
            Todo.id == todo_id
        ).update(
            {
                Todo.title:request.form['title']
            }
        )
        db.session.commit()
        flash('updated task')
        return redirect(url_for('todo.index'))

    return render_template('edit.html',todo = todo)

@todo_bp.route('/<int:todo_id>/done')
def done(todo_id):
    todo = Todo.query.filter(Todo.id == todo_id).first()
    if todo:
        Todo.query.filter(Todo.id == todo_id).update({Todo.status:True})
        db.session.commit()
        flash('task completed')

    return redirect(url_for('todo.index'))

@todo_bp.route('/<int:todo_id>/redo')
def redo(todo_id):
    todo = Todo.query.filter(Todo.id == todo_id).first()
    if todo:
        Todo.query.filter(Todo.id == todo_id).update({Todo.status:False})
        db.session.commit()
        flash('redo task')
        return redirect(url_for('todo.index'))
    return redirect(url_for('todo.index'))

@todo_bp.errorhandler(404)
def page_not_found():
    return render_template('404.html'),404



