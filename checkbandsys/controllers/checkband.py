from flask import Flask,request,redirect,url_for,flash,Blueprint,render_template
from datetime import datetime
from checkbandsys.models import FamousProduct,db
from checkbandsys.forms import CheckForm,AddBand
checkband_blueprint=Blueprint(
    'checkband',
    __name__,
    template_folder='../templates/checkband',
    url_prefix='/checkband'

)

@checkband_blueprint.route('/',methods=('get','post'))
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
        # 如果没有点击查询
        print('else 被执行')
        famousproduct = FamousProduct.query.order_by('add_time DESC').all()
    if request.form.get('btnadd',None) == "add":
        return redirect(url_for('.addband'))
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
        return redirect(url_for(".postdata"))

    elif request.form.get('btnedit',None) == "edit":
        print('修改')



    endpoint='checkband.postdata'
    return render_template(
        'home.html',
        # 把table传输给view了
        endpoint=endpoint,
        data=famousproduct,
        formsearch=formsearch,

    )
# 新增数据控制器
@checkband_blueprint.route('/addband',methods=('post','get'))
def addband():
    addbanddata=AddBand()
    # 如果保存按钮被点击
    if request.form.get('btnsave',None) == "save":
        addnew=FamousProduct()
        addnew.name=addbanddata.name.data
        addnew.description=addbanddata.description.data
        addnew.web=addbanddata.web.data
        addnew.band=addbanddata.band.data
        addnew.add_time=datetime.now()
        addnew.add_person=addbanddata.add_person.data
        db.session.add(addnew)
        try:
            db.session.commit()
        except:
            flash('保存失败')
        return redirect(url_for(".postdata"))
    # 如果取消按钮被点击
    if request.form.get('btnquit',None) == "quit":
        return redirect(url_for(".postdata"))

    return render_template(
        'add.html',
        addbanddata=addbanddata,

    )
# 明细页面
@checkband_blueprint.route('/edit/<int:id>',methods=('post','get'))
def edit(id):
    id=id
    return render_template(
        'edit.html',
        id=id
    )

# 需要新的视图页面（）最好新建一个html控制器
@checkband_blueprint.route('/detail/<int:id>',methods=('post','get'))
def detail(post_id=id):
    pass
