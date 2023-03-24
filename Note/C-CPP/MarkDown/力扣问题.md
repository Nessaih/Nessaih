**1.在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。**

解题思路：矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，因此从左下角开始查找，当要查找数字比左下角数字大时。右移要查找数字比左下角数字小时，上移。（从右上角查找同理，以下为从右上角开始查找）

```c++
//C++版代码实现如下：
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int ym = array.size();
        int xm = array[0].size();
        double k = ym / xm;

        for (int x = xm - 1, y = 0; x >= 0 && y < ym;)
        {
            if (target < array[y][x])
            {
                x--;
            }
            else if (target > array[y][x])
            {
                y++;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};
```

**2.一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。**

解题思路：对于第n项（n >= 3）,有以下规律：

第1次：可以分割成(n-1,1)这两部分台阶，即最后一次只跳一阶,总共跳法有f(n-1)种；

第2次：可以分割成(n-2,2)这两部分台阶，即最后一次只跳二阶,总共跳法有f(n-2)种；

可以推导：f(n) = f(n-1)+f(n-2) (n >= 3)

又因为 f(1) = 1,f(2) = 2，为使f(1),f(2)符合递推公式，可以令f(0) = 1,f(-1) = 0。

则有 f(n) = f(n-1)+f(n-2) (n >= 1)

代码如下：
```C++
class Solution {
public:
    int jumpFloor(int number) {
        int a = 0, b = 1;
        if (number <= 0)
        {
            return 0;
        }
        while (number-- > 0)
        {
            b = a + b;
            a = b - a;
        }
        return b;
    }
};
```

**3.一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。**

解题思路：第n个台阶：

第0次：可以分割成(n,0)这两部分台阶，即一次跳完n节,总共跳法有1种；

第1次：可以分割成(n-1,1)这两部分台阶，即最后一次只跳一阶,总共跳法有f(n-1)种；

第2次：可以分割成(n-2,2)这两部分台阶，即最后一次只跳二阶,总共跳法有f(n-2)种；

...

第n-1次：可以分割成(1,n-1)这两部分台阶，即最后一次只跳n-1阶,总共跳法有f(1)种；

所以,

f(n) = 1 + f(n-1) + f(n-2) + ... + f(2) + f(1) 

    =  f(n-1) + [1 + f(n-2) + ... + f(2) + f(1)]

    = 2 * f(n-1)

```c++
class Solution {
public:
    int jumpFloorII(int number) {
        
        int a = 1;
        while (--number > 0)
        {
            a = a * 2;
        }
        return a;
    }
};
```
由于是2的乘方，可以通过移位运算改进，提高运算效率(实际测试好像没提高，运算还变慢了，只是写法简洁了)

```c++
class Solution {
public:
    int jumpFloorII(int number) {
        return 1 << --number;
    }
};
```
