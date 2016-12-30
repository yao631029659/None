#coding:utf-8
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_wtf import Form
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

# 生成app实例
app = Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)
class FamousProduct(db.Model):
    def __init__(self,name,description):
        self.name=name
        self.description=description
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(10))
    description=db.Column(db.String(255))
    web=db.Column(db.String(255))
    band=db.Column(db.Boolean)
    add_time=db.Column(db.DateTime)
    add_person=db.Column(db.String(10))
    def __repr__(self):
        return '<FamousProduct %s %s>'%(self.name,self.description)


# wtf 验证类
class CheckForm(Form):
    name=StringField(
        'name',
        validators=[DataRequired()]
    )

@app.route('/',methods=('get','post'))
def postdata():
    # 在那里调用就在哪里生成  要不然会报错哦 wit实例
    form = CheckForm()
    # 这句话的意思是 通过验证才能执行啊
    # if form.validate_on_submit():
    #     print('if 被执行')
    #     search='%'+form.name.data+'%'
    #     items=FamousProduct.query.filter(FamousProduct.name.like(search)).all()
    #
    # else:
    #     print('else 被执行')
    #     items=FamousProduct.query.all()
    famousproduct=FamousProduct.query.all()
    endpoint='postdata'

    print(type(id))
    return render_template(
        'home.html',
        # 把table传输给view了
        endpoint=endpoint,
        data=famousproduct,
        form=form

    )

@app.route('/addband',methods=('post','get'))
def addband():
    pass

@app.route('/edit/<int:id>',methods=('post','get'))
def edit(id):
    id=id
    return render_template(
        'edit.html',
        id=id
    )


@app.route('/delete/<int:id>',methods=('post','get'))
def delete():
    print('删除成功')

@app.route('/detail/<int:id>',methods=('post','get'))
def detail():
    print('明细')

if __name__ == '__main__':
    app.run()