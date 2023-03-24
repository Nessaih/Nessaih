
# transform string to float
from functools import reduce
dic = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0, '.':-1}
def str2float(s):
    i = 0
    def f(x,y):
        nonlocal i
        if y == -1:
            i = 1 
            return x
        if i:
            i = i*10
            return x+y/i
        else:
            return x*10+y   
    return reduce(f,map(lambda x:dic[x],s))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
