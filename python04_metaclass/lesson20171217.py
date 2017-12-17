
## 动态创建类

print('start')


class cc(object):
        def __init__(self, name):
            self.name = name
        def say(self):
            print("hello %s" % (self.name,))
cc1 = cc('world')
cc1.say()

print('end')

def otherinit(self, name):
    self.name = name

def othersay(self):
    print("other hello %s" % (self.name,))
DynamicCC = type('DynamicCC',
                 (object,),
                 {"__init__": otherinit, "say":othersay}
                 )
dcc = DynamicCC("other world")
dcc.say()

