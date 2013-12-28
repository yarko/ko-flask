from datetime import datetime

from flask import Flask, render_template, request, jsonify, _app_ctx_stack
# added for MongoKit:
from flask import redirect, url_for
from flask.ext.mongokit import MongoKit, Document

#from sqlite3 import dbapi2 as sqlite3

DATABASE = 'todos.db'
DEBUG = True
SECRET_KEY = 'some super secret development key'

app = Flask(__name__)
app.config.from_object(__name__)

# the data model
class Task(Document):
    __collection__ = 'tasks'
    structure = {
        'title': unicode,
        'description': unicode,
        'creation': datetime,
    }
    required_fields = ['title', 'creation']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True


db = MongoKit(app)
db.register([Task])

# def get_db():
#     return MongoKit(app)

#@app.teardown_appcontext
# def close_database(exception):
#   top = _app_ctx_stack.top
#   if hasattr(top, 'sqlite_db'):
#       top.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def todos():
    entries = db.Task.find()
    return jsonify(tasks=entries)

@app.route('/tasks/new', methods=['GET', 'POST'])
def new_todo():
    if request.method == 'POST':
        task = db.Task()
        task.title = request.json['title']
        task.description = request.json['description']
        task.save()
        return redirect(url_for('index'))
    return jsonify({"title": request.json['title'],
                    "description": request.json['description'],
                     })

if __name__ == '__main__':
    # for debugging w/ wingIDE:
    if __debug__:
        from os import environ
        if 'WINGDB_ACTIVE' in environ:
            app.debug = False  # let wing debugger hangle
    app.run()
