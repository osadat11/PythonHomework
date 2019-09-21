from flask import Blueprint, request, make_response, jsonify
from api.models.task import Task, TaskSchema
import json

task_router = Blueprint('task_router', __name__)

@task_router.route('/tasks', methods=['GET'])
def get_task_list():
    tasks = Task.getTaskList()
    task_schema = TaskSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'tasks' : task_schema.dump(tasks)
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
        'task' : task
    }))

@task_router.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id):
    msg = Task.destroyTask(id)
    print("id : " + str(id) +"  " + str(msg) + " ===> deleted")
    return make_response(jsonify({
        'code': 200,
        'msg' : "task : " + str(msg) + " is deleted"
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
        'task' : task
    }))
