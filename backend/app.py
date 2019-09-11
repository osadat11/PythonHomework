from flask import Flask, request, json, jsonify, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.Text)
    done = db.Column(db.Integer)
    tag = db.Column(db.Text)

    def __repr__(self):
        return '<Task id={id} title={title} description={des} date={date} done={done} tag={tag}>'.format(
            id=self.id, title=self.title, des=self.description, date=self.date, done=self.done, tag=self.tag)

    def __init__(self, *args, **kwargs):
        super(db.Model, self).__init__(*args, **kwargs)
        self.done = 0

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "done": self.done,
            "tag": self.tag
        }


@app.route('/')
def Hello():
    return 'HelloWorld'


@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    result = {
        "tasks": [Task.to_dict(val) for val in Task.query.all()]
    }

    return jsonify(result)


@app.route('/tasks/<int:taskid>', methods=['GET'])
def show_task(taskid):
    task = db.session.query(Task).get(taskid)
    if task == None:
        return "404 not found (´・ω・｀)", 404
    else:
        res = {
            "tasks": Task.to_dict(task)
        }
        return jsonify(res)


@app.route('/tasks/<int:taskid>/delete', methods=['DELETE, POST'])
def delete_task(taskid):
    task = db.session.query(Task).get(taskid)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks')), 204


@app.route('/tasks/create', methods=['POST'])
def create_task():
    title = request.json["tasks"]["title"]
    description = request.json["tasks"]["description"]
    date = request.json["tasks"]["date"]
    done = 0
    tag = request.json["tasks"]["tag"]

    new_task = Task(title, description, date, done, tag)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('tasks')), 204

# タスクの更新画面はプレースホルダーに元のデータがあらかじめ入ってるようにする
@app.route('/tasks/<int:taskid>/edit', methods=['GET'])
def task_editor_set(taskid):
    task = db.session.query(Task).get(taskid)
    res = {
        "tasks": Task.to_dict(task)
    }
    return jsonify(res)

# /tasks/< >/edit でsubmitされた場合 ↓にリダイレクトしてsql更新
@app.route('/tasks/<int:taskid>/update', methods=['PUT'])
def update_task(taskid):
    u_task = db.session.query(Task).get(taskid)

    u_task.title = request.json["tasks"]["title"]
    u_task.description = request.json["tasks"]["description"]
    u_task.date = request.json["tasks"]["date"]
    u_task.done = 0
    u_task.tag = request.json["tasks"]["tag"]

    db.session.add(u_task)
    db.session.commit()

    return redirect(url_for('tasks')), 204


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
