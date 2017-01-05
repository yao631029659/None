#coding:utf-8
from flask import Flask,redirect,url_for
from checkbandsys.controllers.checkband import checkband_blueprint
from checkbandsys.models import db
from checkbandsys.config import DevConfig
from flask_uploads import configure_uploads,UploadSet,IMAGES

def create_app(obj_name):
    app = Flask(__name__)
    app.config.from_object(obj_name)
    db.init_app(app)
    @app.route('/')
    def index():
        return redirect(url_for('checkband.postdata'))
    app.register_blueprint(checkband_blueprint)
    return app
if __name__=="__main__":
    app=create_app('checkbandsys.config.DevConfig')
    app.run()

