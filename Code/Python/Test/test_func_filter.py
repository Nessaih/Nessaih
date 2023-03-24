#除号：//表示向下取整，5//2 = 2;单除号不取整5/2 = 2.5
#程序功能：测试filter函数

#函数功能：判断一个数是否是回数
def is_palindrome(n):
    i = 10
    while(n//i):
        i = i*10
    i = i//10
    while(i>1):
        if(n//i !=  n%10):
            return 0
        n = (n-n//i*i)//10
        i = i//100
    return 1
 
# 测试:

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# print(is_palindrome(12321))
