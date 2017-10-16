## 找出数组中三个数相加为0的所有组合

### 问题描述

找出数组中三个数相加为0的所有组合

**input** [-2,-1,0,1,1,2,3]

**output** [[-2,0,2], [-1,0,1], [-2,-1,3], [-2,1,1]]

### 个人思路

最简单的思路就是三层循环遍历，不过时间复杂度是O(n^3)


### 答案思路

经过排序之后，从第一个元素开始遍历，每次又维护两个指针，分别从当前元素的下一个元素，到末尾元素;如果三个值相加为0，则分别移动两个指针，如果小于0，表示左边元素太大，移动左边指针，否则移动右边指针；注意过滤掉重复元素，即相同元素只取一次。

由于两层循环，所以时间复杂度降为O(n^2)