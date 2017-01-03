from flask_wtf import Form
from wtforms import StringField, SelectField,SubmitField,DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime



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


class FormSave(Form):
    btnsave = SubmitField('save')
    btnquit = SubmitField('quit')
