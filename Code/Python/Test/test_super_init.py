'''
子类构造函数调用super().__init__()的作用：
1.如果子类(Puple)继承父类(Person)不做初始化，那么会自动继承父类(Person)属性name。
2.如果子类(Puple_Init)继承父类(Person)做了初始化，且不调用super初始化父类构造函数，那么子类(Puple_Init)不会自动继承父类的属性(name)。
3.如果子类(Puple_super)继承父类(Person)做了初始化，且调用了super初始化了父类的构造函数，那么子类(Puple_Super)也会继承父类的(name)属性。

'''
class Person:
    def __init__(self,name = "Person",age = 18):
        self.name = name
        self.age = age
        
class Puple(Person):
    pass

class Puple_Init(Person):
    def __init__(self,age):
        self.age = age

class Puple_Super(Person):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)

'''
继承中super的调用顺序(继承中super的调用顺序是与MRO-C3的类方法查找顺序一样的)
'''

class A:
    def __init__(self):
        print('A')
    
class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(A):
    def __init__(self):
        print('D')
        super().__init__()
        
class E(B, C):
    def __init__(self):
        print('E')
        super().__init__()


class F(C, D):
    def __init__(self):
        print('F')
        super().__init__()

class G(E, F):
    def __init__(self):
        print('G')
        super().__init__()

def main():
    #super属性继承测试
    p = Puple()
    pi = Puple_Init(1)
    ps = Puple_Super('fw',1)
    print(p.name)
    #print(pi.name)#运行此句会报错，因为实例Pi没有name这个属性
    print(ps.name)

    #super继承调用顺序测试
    g = G()


if __name__ == '__main__':
    main()
