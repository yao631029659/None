from flask import Flask,request,redirect,url_for,flash,Blueprint,render_template
from datetime import datetime
from checkbandsys.models import FamousProduct,db
from checkbandsys.forms import CheckForm,AddBand
from werkzeug.utils import secure_filename
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
    if request.form.get('search',None)=="search":
        print('formsearch 被执行')
        search='%'+formsearch.name.data+'%'
        famousproduct=FamousProduct.query.filter(FamousProduct.name.like(search)).order_by('add_time DESC').all()
    else:
        # 如果没有点击查询
        print('postdata 的else 被执行')
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
    print('addband 被调用')
    addbanddata=AddBand()
    # 如果保存按钮被点击
    file_url = None
    if request.form.get('btnsave',None) == "save":
        addnew=FamousProduct()
        addnew.name=addbanddata.name.data
        addnew.description=addbanddata.description.data
        addnew.web=addbanddata.web.data
        addnew.band=addbanddata.band.data
        addnew.add_time=datetime.now()
        addnew.add_person=addbanddata.add_person.data
        db.session.add(addnew)
        # secure_filename仅返回ASCII字符。所以， 非ASCII（比如汉字）会被过滤掉，空格会被替换为下划线。
        # print (type(photos))
        # filename = photos.save(addbanddata.photo.data)
        # file_url = photos.url(filename)
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
        file_url=file_url,

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
