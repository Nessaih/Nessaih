### C++语言的for循环执行速度测试
**C++语言的for循环执行速度有多种写法，为了了解哪种写法执行速度更快，使用代码进行测试：**

**（1）VirtualStudio2017执行结果：**
>* (1)Running Time : 4.913
>* (2)Running Time : 8.035
>* (5)Running Time : 0.025


**（2）Gcc 8.1.0 执行结果（clion2020.03.03 + MinGW_x64 8.1.0 ）：**
>* (1)Running Time : 0.065
>* (2)Running Time : 0.192
>* (5)Running Time : 0.153

**结论：**
>* 不同写法的执行速度和编译器有关，总体来说GCC编译器的执行速度更快。


**以下为测试代码：**
```C++
#include <iostream>
#include <vector>
#include <time.h>

void test_speed(size_t m)
{
	std::vector<int> vec(m);
	int k = 0;
	clock_t start,end;
	// 第一种用法：最原始的语法(用下标)
	start = clock();
	for (size_t i = 0; i < vec.size(); ++i) {
		k = vec[i];
	}
	end = clock();
	std::cout << "(1)Running Time : " << (double)(end - start) / CLOCKS_PER_SEC << std::endl;

	
	// 第二种用法：最原始的语法(用迭代器)
	start = clock();
	for (auto it = vec.begin(); it != vec.end(); ++it) {
		k = *it;
	}
	end = clock();
	std::cout << "(2)Running Time : " << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
	// 第三种用法：简化数组遍历语法(从vs2008开始支持)
	/*
	start = clock();
	for each(auto item in vec) {
		k = item;
	}
	end = clock();
	std::cout << "(1)Running Time : " << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
	*/

	// 第四种用法：STL函数
	/*
	start = clock();
	std::for_each(vec.begin(), vec.end(), [](int item) {
		k = item;
	});
	end = clock();
	std::cout << "(1)Running Time : " << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
	*/

	// 第五种用法：C++11新增加的(VS2012支持)
	start = clock();
	for (auto item : vec) {
		k = item;
	}
	end = clock();
	std::cout << "(5)Running Time : " << (double)(end - start) / CLOCKS_PER_SEC << std::endl;
}
int main() {
	test_speed(0xFFFFFF);
	return 0;
}
```
