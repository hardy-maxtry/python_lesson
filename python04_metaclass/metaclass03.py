# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 19:50
# @Author  : Hardy
# @Site    : 
# @File    : metaclass03.py
# @Software: PyCharm


class MetaClassTest3class(type):
    def __new__(cls, clsname, bases, dct):
        dct['test'] = 3
        # dct里有什么
        # return super(MetaClassTest3class, cls).__new__(cls, clsname, bases, dct)
        return type.__new__(cls, clsname, bases, dct)

class Foo():

    pass

class FooChild(Foo, metaclass = MetaClassTest3class):
    # pass
    id = 1
    name = "hardy"
    def fn(self):
        print('fn')
    pass

f = FooChild()
print(f.test)
f.fn()