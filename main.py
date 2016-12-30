#coding:utf-8
from flask import Flask
# 下面两个是给表格用的
from flask_table import Table, Col
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

    name=db.Column(db.String(255),primary_key=True)
    description=db.Column(db.String(255))

    def __repr__(self):
        return '<FamousProduct %s %s>'%(self.name,self.description)

# html表格
class ShowTable(Table):
    # 这个是保留字 会给table增加class属性
    classes = ['table','table-border','table-sriped','table-hover','table-condensed']
    # 这个表两个列
    name = Col('Name')
    description = Col('Description')


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
    if form.validate_on_submit():
        print('if 被执行')
        search='%'+form.name.data+'%'
        items=FamousProduct.query.filter(FamousProduct.name.like(search)).all()

    else:
        print('else 被执行')
        items=FamousProduct.query.limit(10).all()
    return render_template(
        'home.html',
        # 把table传输给view了
        table=ShowTable(items),
        form=form
    )
    # print(table.__html__())

@app.route('/addband',methods=('post','get'))
def addband():
    pass

if __name__ == '__main__':
    app.run()