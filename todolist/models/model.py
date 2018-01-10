#encoding:utf8

from todolist.exts import db
from datetime import datetime

__all__ = ['Todo']   #规定外部导入的名称

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    posted_on = db.Column(db.Date,default=datetime.now)
    status = db.Column(db.Boolean(),default=False)

    def __init__(self, *args,**kwargs):
        super(Todo,self).__init__(*args,**kwargs) #定义初始化函数

    def __repr__(self):
        return "<Todo %s>"%self.title

    def store_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_todo(self):
        db.session.delete(self)
        db.session.commit()


