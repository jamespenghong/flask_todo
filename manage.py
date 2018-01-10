#encoding:utf8

from todolist import create_app
from todolist.exts import db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('runserver',Server(host='127.0.0.1',port=5000))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()