# 生成app实例
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
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
