from api.database import db, ma


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    due_d = db.Column(db.String(10), nullable=True)
    due_t = db.Column(db.String(5), nullable=True)
    priority = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.name

    def getTaskList():
        task_list = db.session.query(Task).all()

        if task_list == None:
            return []
        else:
            return task_list

    def registTask(task):
        record = Task(
            title=task['title'],
            due_d=task['dueD'],
            due_t=task['dueT'],
            priority=task['priority']
        )
        db.session.add(record)
        db.session.commit()

        return task

    
    def destroyTask(taskID):
        selectedTask = db.session.query(Task).filter(Task.id == taskID).one()
        msg = selectedTask.title

        db.session.delete(selectedTask)
        db.session.commit()

        return msg


    def updateTask(task, taskID):
        record = Task(
            title=task['title'],
            due_d=task['dueD'],
            due_t=task['dueT'],
            priority=task['priority']
        )
        base_task = db.session.query(Task).filter(Task.id == taskID).first()
        base_task.title = record.title
        base_task.due_d = record.due_d
        base_task.due_t = record.due_t
        base_task.priority = record.priority
        db.session.commit()
        return task


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
        fields = ('id', 'title', 'due_d', 'due_t', 'priority')
