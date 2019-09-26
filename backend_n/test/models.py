from .backend import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    # description = db.Column(db.Text)
    # date = db.Column(db.Text)
    # done = db.Column(db.Integer)
    # tag = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            # "description": self.description,
            # "date": self.date,
            # "done": self.done,
            # "tag": self.tag
        }

    # def __repr__(self):
    #     return '<Task id={id} title={title} description={des} date={date} done={done} tag={tag}>'.format(
    #         id=self.id, title=self.title, des=self.description, date=self.date, done=self.done, tag=self.tag)
    
    def __repr__(self):
        return '<Task id={id} title={title!r}>'.format(
            id=self.id, title=self.title)


def init():
    db.create_all()