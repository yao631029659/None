from flask_script import Manager,Server

from checkbandsys.models import db,FamousProduct
from checkbandsys.init import app

manager=Manager(app)
manager.add_command('server',Server())

@manager.shell
def make_shell_content():
    return dict(app=app,db=db,FamousProduct=FamousProduct)

if __name__ == '__main__':
    manager.run()




