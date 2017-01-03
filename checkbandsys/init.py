#coding:utf-8
from flask import Flask,redirect,url_for
from checkbandsys.controllers.checkband import checkband_blueprint

from checkbandsys.models import db
from checkbandsys.config import DevConfig
app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('checkband.postdata'))

app.register_blueprint(checkband_blueprint)
if __name__=="__main__":
    app.run()

