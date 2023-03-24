

#FileName:ListComprehesion.py

'''
列表解析式（也称列表推导式），用法如下：

    列表解析式的用法很好理解，可以简单地看成两部分。红色虚线后
面的是我们熟悉的 for 循环的表达式，而虚线前面的可以认为是我们
想要放在列表中的元素，在这个例子中放在列表中的元素即是后面循环
元素本身。

             ┊
list = [item ┊ for item in iterable]
             ┊

'''
#############################打印当前代码################################
import os
#path = os.getcwd()#获取当前文件夹路径 
path = os.path.realpath('ListComprehesion.py')#获取当前文件路径 
file_handle = open(path,encoding='utf-8')
line =  file_handle.readline()
while(line):
    print(line,end = ' ')
    line =  file_handle.readline()
file_handle.close()
#############################打印当前代码################################


#question：现在我们有十个元素要装进列表中，普通的写法是这样的：
a = []
for i in range(1,11):
    a.append(i)

#下面换成列表解析式的方式来写：
b = [i for i in range(1,11)]

#普通写法与列表解析式写法执行效率对比（列表解析式执行效率高于前者）
import time 
c = []
t0 = time.clock()
for i in range(1,20000):
    c.append(i)
print("\n普通写法：",time.clock()-t0," second")

t0 = time.clock()
d = [i for i in range(1,20000)]
print("列表解析式：",time.clock()-t0," second\n")
#某一次的执行结果：
#普通写法： 0.004980784404344525  second
#列表解析式： 0.000740819759672098  second


#为更好的理解列表解析式的用法，继续看几个例子：
a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n%2 == 0]
z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print('list_a:',a,'\n'\
      'list_c:',c,'\n'\
      'list_k:',k,'\n'\
      'list_z:',z,'\n')

#################################################################

#字典推导式的方式略有不同，主要式因为创建字典必须满足‘键-值’的两个条件，例子如下：
d = {i:i+i for i in range(4)}
g = {i:j for i,j in zip(range(1,6),'abcde')}
h = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print('dictionary_d:',d,'\n'\
      'dictionary_g:',g,'\n'\
      'dictionary_h:',h,'\n')
      
      
