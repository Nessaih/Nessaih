
## 一、设计哈希集合
不使用任何内建的哈希表库设计一个哈希集合

实现 MyHashSet 类：

+ add(value)：向哈希集合中插入一个值。
+ contains(value) ：返回哈希集合中是否存在这个值。
+ remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

**示例:**
```C++
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）

```

**提示：**

+ 0 <= key <= 106
+ 最多调用 104 次 add、remove 和 contains 。

### 题解：
```C++

#include <iostream>


using namespace std;

class MyHashSet {
private:
#define HASHSIZE  101

	typedef struct hashnode {
		int key;
		struct hashnode *next;
	}HashNode;

	HashNode *hashtab[HASHSIZE];

	int hash(int  key)
	{
		key = key % HASHSIZE;
		return key;
	}

public:
	/** Initialize your data structure here. */
	MyHashSet() {
		for (int i = 0; i < HASHSIZE; ++i)
		{
			hashtab[i] = NULL;
		}
	}

	void add(int key)
	{
		int hashkey = hash(key);
		HashNode *p = hashtab[hashkey];

		while (p)
		{
			if (key == p->key)
				return;         //the key already exist
			else
				p = p->next;
		}
		if (p = (HashNode *)malloc(sizeof(HashNode)))
		{
			p->key = key;
			p->next = hashtab[hashkey];
			hashtab[hashkey] = p;
		}
	}

	void remove(int key)
	{
		int hashkey = hash(key);
		HashNode *p = hashtab[hashkey];
		HashNode *h = NULL;

		if (p)
		{
			if (key == p->key)
			{
				hashtab[hashkey] = p->next;
				free(p);
				p = NULL;			//Preventing the execution of while(p)
			}
			else
			{
				h = p;
				p = p->next;
			}
		}
		while (p)
		{
			if (key == p->key)
			{
				h->next = p->next;
				free(p);
				p = NULL;
			}
			else
			{
				h = p;
				p = p->next;
			}
		}
	}

	/** Returns true if this set contains the specified element */
	bool contains(int key)
	{
		int hashkey = hash(key);
		HashNode *p = hashtab[hashkey];

		while (p)
		{
			if (key == p->key)
				return true;
			else
				p = p->next;
		}
		return false;
	}
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */

int main()
{

	MyHashSet hashSet = MyHashSet();
	hashSet.add(1);
	hashSet.add(2);
	cout << hashSet.contains(1);  // 返回 true
	cout << hashSet.contains(3);  // 返回 false (未找到)
	hashSet.add(2);
	cout << hashSet.contains(2);  // 返回 true
	hashSet.remove(2);
	cout << hashSet.contains(2);  // 返回  false (已经被删除)
}
 
```
---

## 二、设计哈希映射

不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

+ MyHashMap() 用空映射初始化对象
+ void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
+ int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
+ void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

**示例：**
```C++
输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
```

**提示：**
+ 0 <= key, value <= 106
+ 最多调用 104 次 put、get 和 remove 方法
 
### 题解：
```C++

class MyHashMap {

private:
    #define HASHSIZE  101
    typedef struct hashnode {
        int key;
        int value;
        struct hashnode *next;
    }HashNode;

    HashNode *hashtab[HASHSIZE];

    int hash(int  key)
    {
        key = key % HASHSIZE;
        return key;
    }

public:
    /** Initialize your data structure here. */
    MyHashMap() {
        for (int i = 0; i < HASHSIZE; ++i)
        {
            hashtab[i] = NULL;
        }
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int hashkey = hash(key);
        HashNode *p = hashtab[hashkey];

        while (p)
        {
            if (key == p->key)  //the key already exist,update the value
            {
                p->value = value;
                return ;
            }         
            else
            {
                p = p->next;
            }
        }
        //the key not exist,create a new node
        if (p = (HashNode *)malloc(sizeof(HashNode)))
        {
            p->key = key;
            p->value = value;
            p->next = hashtab[hashkey];
            hashtab[hashkey] = p;
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int hashkey = hash(key);
        HashNode *p = hashtab[hashkey];

        while (p)
        {
            if (key == p->key)
                return p->value;
            else
                p = p->next;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int hashkey = hash(key);
        HashNode *p = hashtab[hashkey];
        HashNode *h = NULL;

        if (p)
        {
            if (key == p->key)
            {
                hashtab[hashkey] = p->next;
                free(p);
                p = NULL;           //Preventing the execution of while(p)
            }
            else
            {
                h = p;
                p = p->next;
            }
        }
        while (p)
        {
            if (key == p->key)
            {
                h->next = p->next;
                free(p);
                p = NULL;
            }
            else
            {
                h = p;
                p = p->next;
            }
        }
    }
};


```
---

## 三、官方参考答案

这里给出 C++ 的解决方案供您参考。在我们的解决方案中，我们使用一个数组来表示哈希集。数组中的每个元素都是一个桶。在每个桶中，我们使用数组列表 array list（或 C++ 中的向量 vector）来存储所有值。


**哈希集合：**
```C++
#define MAX_LEN 100000          // the amount of buckets
class MyHashSet {
private:
    vector<int> set[MAX_LEN];   // hash set implemented by array
    
    /** Returns the corresponding bucket index. */
    int getIndex(int key) {
        return key % MAX_LEN;
    }
    
    /** Search the key in a specific bucket. Returns -1 if the key does not existed. */
    int getPos(int key, int index) {
        // Each bucket contains a list. Iterate all the elements in the bucket to find the target key.
        for (int i = 0; i < set[index].size(); ++i) {
            if (set[index][i] == key) {
                return i;
            }
        }
        return -1;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        
    }
    
    void add(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            // Add new key if key does not exist.
            set[index].push_back(key);
        }
    }
    
    void remove(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            // Remove the key if key exists.
            set[index].erase(set[index].begin() + pos);
        }
    }
    
    /** Returns true if this set did not already contain the specified element */
    bool contains(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        return pos >= 0;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * bool param_3 = obj.contains(key);
 */
```

**哈希映射：**
```C++
#define MAX_LEN 100000            // the amount of buckets

class MyHashMap {
private:
    vector<pair<int, int>> map[MAX_LEN];       // hash map implemented by array
    
    /** Returns the corresponding bucket index. */
    int getIndex(int key) {
        return key % MAX_LEN;
    }
    
    /** Search the key in a specific bucket. Returns -1 if the key does not existed. */
    int getPos(int key, int index) {
        // Each bucket contains a vector. Iterate all the elements in the bucket to find the target key.
        for (int i = 0; i < map[index].size(); ++i) {
            if (map[index][i].first == key) {
                return i;
            }
        }
        return -1;
    }
    
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        
    }
    
    /** value will always be positive. */
    void put(int key, int value) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            map[index].push_back(make_pair(key, value));
        } else {
            map[index][pos].second = value;
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            return -1;
        } else {
            return map[index][pos].second;
        }
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            map[index].erase(map[index].begin() + pos);
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

我们来看看 “删除” 操作。在找到元素的位置之后，我们需要从数组列表中删除元素。

假设我们要删除第 i 个元素，并且数组列表的大小为 n。

内置函数中使用的策略是把第 i 个元素后的所有元素向前移动一个位置。也就是说，你必须移动 n - i 次。因此，从数组列表中删除元素的时间复杂度将为 O(n)。

考虑 i 取不同值的情况。平均而言，我们将移动 ((n - 1) + (n - 2) + ... + 1 + 0) / n = (n - 1) / 2 次。

 

希望有两种解决方案可以将时间复杂度从 O(n) 降低到 O(1)。

**1. 交换**

我们可以使用一种巧妙的策略。首先，用存储桶中的最后一个元素交换要移除的元素。然后删除最后一个元素。通过这种方法，我们成功地在 O(1) 的时间复杂度中去除了元素。

**2. 链表**

实现此目标的另一种方法是使用链表而不是数组列表。通过这种方式，我们可以在不修改列表中的顺序的情况下删除元素。该策略时间复杂度为 O(1)。

 ---

## 四、复杂度分析


如果总共有 M 个键，那么在使用哈希表时，可以很容易地达到 O(M) 的空间复杂度。

但是，你可能已经注意到哈希表的时间复杂度与设计有很强的关系。

我们中的大多数人可能已经在每个桶中使用数组来将值存储在同一个桶中，理想情况下，桶的大小足够小时，可以看作是一个常数。插入和搜索的时间复杂度都是 O(1)。

但在最坏的情况下，桶大小的最大值将为 N。插入时时间复杂度为 O(1)，搜索时为 O(N)。


#### 内置哈希表的原理

**内置哈希表的典型设计是：**

 + 键值可以是任何可哈希化的类型。并且属于可哈希类型的值将具有哈希码。此哈希码将用于映射函数以获取存储区索引。
 + 每个桶包含一个数组，用于在初始时将所有值存储在同一个桶中。
 + 如果在同一个桶中有太多的值，这些值将被保留在一个高度平衡的二叉树搜索树中。
 + 插入和搜索的平均时间复杂度仍为 O(1)。最坏情况下插入和搜索的时间复杂度是 O(logN)，使用高度平衡的 BST。这是在插入和搜索之间的一种权衡。



