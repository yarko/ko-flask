from datetime import datetime

from flask import Flask, render_template, request, jsonify, _app_ctx_stack
# added for MongoKit:
from flask import redirect, url_for
from flask.ext.mongokit import MongoKit, Document

# from flask_debugtoolbar import DebugToolbarExtension

#from sqlite3 import dbapi2 as sqlite3

DATABASE = 'todos.db'
DEBUG = True
SECRET_KEY = 'some super secret development key'

app = Flask(__name__)
app.config.from_object(__name__)

# toolbar = DebugToolbarExtension(app)

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

def mongoify(*args, **kwargs):
    """Creates a :class:`~flask.Response` with the JSON representation of
    the given arguments with an `application/json` mimetype.  The arguments
    to this function are the same as to the :class:`dict` constructor.

    Example usage::

        @app.route('/_get_current_user')
        def get_current_user():
            return jsonify(username=g.user.username,
                           email=g.user.email,
                           id=g.user.id)

    This will send a JSON response like this to the browser::

        {
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
        }

    This requires Python 2.6 or an installed version of simplejson.  For
    security reasons only objects are supported toplevel.  For more
    information about this, have a look at :ref:`json-security`.

    .. versionadded:: 0.2
    """
    return app.response_class(dict(*args, **kwargs), mimetype='application/json')

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
    tasks = list(entries)
    for i in tasks:
        i.pop(u'_id')
    # return jsonify(tasks=list(entries))
    # return jsonify(tasks=[i.to_json() for i in tasks])
    return mongoify(tasks=[i.to_json() for i in tasks])

@app.route('/tasks/new', methods=['GET', 'POST'])
def new_todo():
    if request.method == 'POST':
        task = db.Task()   # create, w/ default creation;
        ## one of two ways:
        rtask = request.json   # creation is not part of it
        # rtask.pop('creation')
        ## alternately, could have done this:
        # rtask = {}
        # rtask.title = request.json['title']
        # rtask.description = request.json['description']
        task.update(rtask)     # update desired fields
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
