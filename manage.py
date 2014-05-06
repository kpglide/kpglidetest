from flask.ext.script import Manager
from app import app, db

manager = Manager(app)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()