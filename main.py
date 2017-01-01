#coding:utf-8
import urllib.parse
import datetime
from flask import Flask,request,redirect,url_for,flash
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_wtf import Form
from wtforms import StringField,TextAreaField,SelectField,SubmitField,DateTimeField
from wtforms.validators import DataRequired

# 生成app实例
app = Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)
class FamousProduct(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(10))
    description=db.Column(db.String(255))
    web=db.Column(db.String(255))
    band=db.Column(db.Boolean())
    add_time=db.Column(db.DateTime())
    add_person=db.Column(db.String(10))
    def __repr__(self):
        return '<FamousProduct %s %s>'%(self.name,self.description)


# wtf 验证类
class CheckForm(Form):
    name=StringField(
        'name',
        validators=[DataRequired()]
    )
    search=SubmitField('查询',render_kw={'class':'btn btn-primary'})
    btnadd = SubmitField('add', render_kw={'class': 'btn btn-primary'})
    btndel = SubmitField('del',render_kw={'class':'btn btn-primary'})
# 用于crud跳转


# addhtml用的数据
class AddBand(Form):
    name=StringField(
        '品牌名',
        validators=[DataRequired]
    )
    description = StringField(
        '描述',
        validators=[DataRequired()]
    )
    web = StringField(
        '网站',
        validators=[DataRequired()]
    )
    band = SelectField(
        '是否品牌',
        choices=[(True,'是'),(False,'否')]
    )
    add_time = DateTimeField(
        '添加时间',
        format='%Y-%m-%d %H:%M:%S',
        default=datetime.datetime.now(),
        # 禁止编辑
        render_kw={'disabled':''},
        validators=[DataRequired()]
    )
    add_person = StringField(
        '添加人员',
        validators=[DataRequired()]
    )
    btnsave = SubmitField(
        'save',
        render_kw={'class':'btn btn-primary'}
    )
    btnquit=SubmitField(
        'quit',
        render_kw={'class': 'btn btn-primary'}
    )


class FormSave(Form):
    btnsave = SubmitField('save')
    btnquit = SubmitField('quit')


@app.route('/',methods=('get','post'))
def postdata():
    # 在那里调用就在哪里生成  要不然会报错哦 wit实例
    formsearch = CheckForm()
    # 这句话的意思是 通过验证才能执行啊

    # 查询被执行
    if formsearch.validate_on_submit():
        print('formsearch 被执行')
        search='%'+formsearch.name.data+'%'
        famousproduct=FamousProduct.query.filter(FamousProduct.name.like(search)).order_by('add_time DESC').all()
    else:
        print('else 被执行')
        famousproduct = FamousProduct.query.order_by('add_time DESC').all()
    if request.form.get('btnadd',None) == "add":
        return redirect(url_for('addband'))
    elif request.form.get('btndel', None) == "del":
        print("你点击了删除")
        choicelist = request.form.getlist('to_operate')
        print(choicelist)
        for item in choicelist:
            item=int(item)
            # FamousProduct.query.filter_by(id=item).delete()
            deleteitem=FamousProduct.query.get(item)
            db.session.delete(deleteitem)
        db.session.commit()
        return redirect(url_for("postdata"))

    elif request.form.get('btnedit',None) == "edit":
        print('修改')



    endpoint='postdata'
    return render_template(
        'home.html',
        # 把table传输给view了
        endpoint=endpoint,
        data=famousproduct,
        formsearch=formsearch,

    )
# 新增数据控制器
@app.route('/addband',methods=('post','get'))
def addband():
    addbanddata=AddBand()
    # 如果保存按钮被点击
    if request.form.get('btnsave',None) == "save":
        addnew=FamousProduct()
        addnew.name=addbanddata.name.data
        addnew.description=addbanddata.description.data
        addnew.web=addbanddata.web.data
        addnew.band=addbanddata.band.data
        addnew.add_time=datetime.datetime.now()
        # addnew.add_time=datetime.datetime.now()
        addnew.add_person=addbanddata.add_person.data
        db.session.add(addnew)
        try:
            db.session.commit()
        except:
            flash('保存失败')
        return redirect(url_for("postdata"))
    # 如果取消按钮被点击
    if request.form.get('btnquit',None) == "quit":
        return redirect(url_for("postdata"))

    return render_template(
        'add.html',
        addbanddata=addbanddata,

    )

@app.route('/edit/<int:id>',methods=('post','get'))
def edit(id):
    id=id
    return render_template(
        'edit.html',
        id=id
    )

# 需要新的视图页面（）最好新建一个html控制器
@app.route('/detail/<int:id>',methods=('post','get'))
def detail(post_id=id):
    pass

if __name__ == '__main__':
    app.run()