## 找出数组中三个数相加最接近某个数的结果

### 问题描述

找出数组中三个数相加最接近某个数的结果

**input** [-1,2,1,-4]  1

**output** -1+1+2 = 2

### 个人思路

有了计算三个数相加为0的基础，计算接近某个数就简单很多。同样的算法，不过将与0的比较改为与target的比较；注意的是，这次容许重复的值出现。
