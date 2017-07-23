leetcode
========

在leetcode刷题之路,主要记录解题思路及部分代码(python实现)。

000.twoSum
给定一个整数列表和一个整数，求两个列表元素相加等于输入整数的索引地址；假定结果唯一且不使用相同元素两次。

输入:
列表 [2, 7, 11, 15]
整数 9

输出：
索引 [0, 1]

思路：
首先想到的是暴力破解，即使用两次循环遍历出结果，此方法对应
twoSum1, 由于使用两层循环，时间复杂度为O(n^2),空间复杂度为
O(1)，即不使用额外空间。

我个人想到这里就开始提交代码，看了答案发现还有一个使用
哈希表的方法，在遍历的时候使用哈希表存储其所对应的元素及
索引，这样可以一次循环就找到结果，时间复杂度为O(n),空间
复杂度为O(n),因为存储了所有元素。

这道题考察的是哈希表的应用，在使用暴力破解等直观方法解题后，
应考虑能否以及如何降低算法的复杂度。