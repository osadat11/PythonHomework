from flask import Blueprint, request, make_response, jsonify
from flask_cors import cross_origin
from api.models.task import Task, TaskSchema
from api.lib import format_to_json as FTJ
import json

task_router = Blueprint('task_router', __name__)


@task_router.route('/tasks', methods=['GET'])
def get_task_list():
    done_tasks = []
    base_tasks = []
    tasks = Task.getTaskList()
    schema = TaskSchema(many=True)
    allTasks = schema.dump(tasks)
    for index in range(len(allTasks)):
        if allTasks[index]['done'] == 1:
            done_tasks.append(allTasks[index])
        else:
            base_tasks.append(allTasks[index])

    msg1 = ""
    msg2 = ""

    if base_tasks == []:
        msg1 = "None"
    if done_tasks == []:
        msg2 = "None"

    return make_response(jsonify({
        'code': 200,
        'tasks': base_tasks,
        'done': done_tasks,
        'msg': {
            "msg_task": msg1,
            "msg_done": msg2
        }
    }))


@task_router.route('/tasks', methods=['POST'])
def registTask():
    jsonData = json.dumps(request.json)
    taskData = json.loads(jsonData)
    print(taskData)

    task = Task.registTask(taskData)
    task_schema = TaskSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'task': task
    }))


@task_router.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id):
    msg = Task.destroyTask(id)
    print("id : " + str(id) + "  " + str(msg) + " ===> deleted")
    return make_response(jsonify({
        'code': 200,
        'msg': "task : " + str(msg) + " is deleted"
    }))


@task_router.route('/tasks/<int:id>', methods=['PUT'])
def updateTask(id):
    jsonData = json.dumps(request.json)
    taskData = json.loads(jsonData)
    print(taskData)

    task = Task.updateTask(taskData, id)
    task_schema = TaskSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'task': task
    }))
