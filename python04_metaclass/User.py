# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 20:17
# @Author  : Aries
# @Site    : 
# @File    : User.py
# @Software: PyCharm

from MyModel import Model
from Field import IntegerField, StringField
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
# User.id
# u.id
# u['id']
u = dict(id=1,password="aaa")
# u = User.find(1)