from flask_script import Manager,Server
from checkbandsys import create_app
from checkbandsys.models import db,FamousProduct

# 也可以从环境变量里面读取
app = create_app('checkbandsys.config.DevConfig')

manager=Manager(app)
manager.add_command('server',Server())

@manager.shell
def make_shell_content():
    return dict(app=app,db=db,FamousProduct=FamousProduct)

if __name__ == '__main__':
    manager.run()




