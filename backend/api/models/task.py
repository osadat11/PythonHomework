from api.database import db, ma


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    due_d = db.Column(db.String(10), nullable=True)
    due_t = db.Column(db.String(5), nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(180), nullable=True)
    done = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<id={id}, title={title!r} due_d={due_d!r}, due_t={due_t!r}, priority={priority}, description={description!r}. done={done}>'.format(
            id=self.id, title=self.title, due_d=self.due_d, due_t=self.due_t, priority=self.priority, description=self.description, done=self.done
        )

    def getTaskList():
        task_list = db.session.query(Task).all()
        # print(task_list)
        # for task in task_list:
        #     print(task.title)
        # input()
        if task_list == None:
            return []
        else:
            return task_list

    def registTask(task):
        record = Task(
            title=task['title'],
            due_d=task['dueD'],
            due_t=task['dueT'],
            priority=task['priority'],
            description=task['description'],
            done=0
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
            priority=task['priority'],
            description=task['description'],
            done=task['done']
        )
        base_task = db.session.query(Task).filter(Task.id == taskID).first()
        base_task.title = record.title
        base_task.due_d = record.due_d
        base_task.due_t = record.due_t
        base_task.priority = record.priority
        base_task.due_t = record.description
        base_task.done = record.done
        db.session.commit()
        return task


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
