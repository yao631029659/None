from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField,SubmitField,DateTimeField,FileField
from wtforms.validators import DataRequired
from datetime import datetime
from . import img
# from  . import photos
# 实例化

# wtf 验证类
class CheckForm(Form):
    name=StringField(
        'name',
        validators=[DataRequired()]
    )
    search=SubmitField('search',render_kw={'class':'btn btn-primary'})
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
        default=datetime.now(),
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
    photo = FileField(u'图片上传')
    # photo=FileField(u'图片上传',validators=[FileAllowed(photos,u'只能上传图片！'),FileRequired(u'文件未选择')])




class FormSave(Form):
    btnsave = SubmitField('save')
    btnquit = SubmitField('quit')
