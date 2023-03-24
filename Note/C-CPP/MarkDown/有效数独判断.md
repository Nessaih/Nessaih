### 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

>* 注意：
>* 一个有效的数独（部分已被填充）不一定是可解的。
>* 只需要根据以上规则，验证已经填入的数字是否有效即可。

示例 1：

<!--注释此图片插入方式，因为不支持图片缩放
    ![picture2](https://github.com/Nessaih/C-CPP/blob/main/pictures/LC_isValidSudoku_2.png)
-->

<img src="https://github.com/Nessaih/C-CPP/blob/main/pictures/LC_isValidSudoku_2.png" width = "75%" height = "75%" alt="picture2" align=center />

**输入：**
```
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**输出：**`true`

示例 2：

**输入：**
```board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**输出：**`false`
**解释：**除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。


---

#### 解题思路

+ 分三次遍历数据的每一行、每一列和每一个子数独，需要循环`9 * 9 * 3 = 243`次，而实际上三次遍历可以在一次迭代中完成。
+ 使`i = 0 ~ 8,j = 0 ~ 8` ,取坐标位置`(i,j)、(j,i)`可以分别完成行和列的遍历，难点在于如何设计每块的数组下表位置更新。
+ 记每块的数据为`(x,y)`,只需要令`x = [i/3*3+j/3] , y = [i%3*3+j%3]`,则可实现依次对每块（子数独）的遍历。

<!--注释此图片插入方式，因为不支持图片缩放
    ![picture1](https://github.com/Nessaih/C-CPP/blob/main/pictures/LC_isValidSudoku_1.png)
-->
<img src="https://github.com/Nessaih/C-CPP/blob/main/pictures/LC_isValidSudoku_1.png" width = "50%" height = "50%" alt="picture1" align=center />


**扩展--观察规律，可以发现：**

>* 对于长度为`(n^2) * (n^2)`大小的数组，需要对每个子块`n*n`依次遍历，只需要令遍历坐标`(x,y) = ([i/n*n+j/n], [i%n*n+j%n])`即可。

**题解：**
```C++
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> row,column,block;

        for (char i = 0; i < 9; ++i) {
            row.clear();
            column.clear();
            block.clear();
            for (char j = 0; j < 9; ++j) {
                /* check every row */
                if (row.count(board[i][j]) > 0)
                    return false;
                else if ('.' != board[i][j])
                    row.insert(board[i][j]);
                /* check every column */
                if (column.count(board[j][i]) > 0)
                    return false;
                else if ('.' != board[j][i])
                    column.insert(board[j][i]);

                /* check every block */
                if (block.count(board[i/3*3+j/3][i%3*3+j%3]) > 0)
                    return false;
                else if ('.' != board[i/3*3+j/3][i%3*3+j%3])
                    block.insert(board[i/3*3+j/3][i%3*3+j%3]);
            }
        }
        return true;
    }
};
vector<vector<char>> str2vec(char str[9][9]){
    vector<char> ele;
    vector<vector<char>> res;
    for (char i = 0; i < 9; ++i) {
        ele.clear();
        for (char j = 0; j < 9; ++j) {
            ele.push_back(str[i][j]);
        }
        res.push_back(ele);
    }
    return res;
}
int main() {

     char s[9][9] = {{'5','3','.','.','7','.','.','.','.'},
                    {'6','.','.','1','9','5','.','.','.'},
                    {'.','9','8','.','.','.','.','6','.'},
                    {'8','.','.','.','6','.','.','.','3'},
                    {'4','.','.','8','.','3','.','.','1'},
                    {'7','.','.','.','2','.','.','.','6'},
                    {'.','6','.','.','.','.','2','8','.'},
                    {'.','.','.','4','1','9','.','.','5'},
                    {'.','.','.','.','8','.','.','7','9'}};
    vector<vector<char>> cv = str2vec(s);
    Solution sl;
    cout << sl.isValidSudoku(cv);

    return 0;
}

```
