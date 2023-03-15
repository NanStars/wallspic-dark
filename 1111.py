class Person:
    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight


    def name(self):
        return '[我的名字是：%s]' % self.__name

    # 用property装饰的方法名.setter，这样就可以修改了

    def name(self, new_name):
        # if not isinstance(new_name,str):
        if type(new_name) is not str:
            raise Exception('改不了')
        if new_name.startswith('sb'):
            raise Exception('不能以sb开头')
        self.__name = new_name


p = Person('xc', 1.82, 70)
# 按照属性进行调用
print(p.name)  # 调用property装饰器后的方法 name，变为一个属性
# 按照属性进行调用，并修改
p.name = 'pppp'  # 调用property.setter装饰器后的方法，可以进行修改

# 改不了，直接抛异常
# p.name=999
# p.name='sb_xxx'
