leetcode
========

在leetcode刷题之路,主要记录解题思路及部分代码(python实现)。

[000.twoSum](https://github.com/tigeroses/leetcode/blob/master/000.twoSum/README.md)

给定一个整数列表和一个整数，求两个列表元素相加等于输入整数的索引地址；假定结果唯一且不使用相同元素两次。

输入:
列表 [2, 7, 11, 15]
整数 9

输出：
索引 [0, 1]

[001.addTwoNumbers](https://github.com/tigeroses/leetcode/blob/master/001.addTwoNumbers/README.md)

两个单向链表，存储两个整数；链表每个节点存储一个非负整数，且逆序存储，要求计算两个链表的和

**Input**: (2 -> 4 -> 3) + (5 -> 6 -> 4)

**Output**: 7 -> 0 -> 8

[002.lengthOfLongestSubstring](https://github.com/tigeroses/leetcode/blob/master/002.lengthOfLongestSubstring/README.md)

给定一个字符串，找到不含重复元素的最长子串

**Input** "abcabcbb"

**Output** 3

**Input** "bbbbb"

**Output** 1

[003.findMedianSortedArrays](https://github.com/tigeroses/leetcode/blob/master/003.findMedianSortedArrays/README.md)

给定两个有序数组，长度分别m和n，寻找两个有序数组的中位数，时间复杂度要在O(log(m+n))

**Input** [1, 3] [2]

**Output** 2.0

**Input** [1, 2] [3, 4]

**Output** 2.5

[004.longestPalindrome](https://github.com/tigeroses/leetcode/blob/master/004.longestPalindrome/README.md)

给定字符串，找到其中最长回文

**Input** "babad"

**Output** "bab"

**Input** "aaaa"

**Output** "aaaa"

[005.zigZagConvert](https://github.com/tigeroses/leetcode/blob/master/005.zigZagConvert/README.md)

对ZigZag格式进行转换

**Input** 

A   E
B D F
C

行数3

**Output** AEBDFC

[006.reverseInteger](https://github.com/tigeroses/leetcode/blob/master/006.reverseInteger/README.md)

反转给定整数，如果超出32bit则返回0

**Input** 100

**Output** 1

**Input** -101

**Output** -101

[007.myAtoi](https://github.com/tigeroses/leetcode/blob/master/007.myAtoi/README.md)

实现atoi函数，将字符串转换为整型

**Input** '123'

**Output** 123

**Input** '  -123cd'

**Output** -123

[008.palindromeNumber](https://github.com/tigeroses/leetcode/blob/master/008.palindromeNumber/README.md)

判断数字是否符合回文规则

**Input** 12321

**Output** True

**Input** 1231

**Output** False

[009.regularExpressionMatching](https://github.com/tigeroses/leetcode/blob/master/009.regularExpressionMatching/README.md)

实现正则匹配的. * 功能

. 表示任意的一个字符

\* 表示前面的单个字符重复n次，n可为0

**Input** isMatch('aa', 'a')

**Output** False

**Input** isMatch('aa', 'aa')

**Output** True

**Input** isMatch('aa', 'a\*')

**Output** True

**Input** isMatch('aab', 'c\*a\*b\*')

**Output** True

[010.containerWithMostWater](https://github.com/tigeroses/leetcode/blob/master/010.containerWithMostWater/README.md)

给一组二维坐标的点，x从1开始递增，y是随机的正整数，每个点有垂直横坐标的线段，求两条线围成的容器哪个装的水更多。

**input** [1,1]

**output** 1

[011.integerToRoman](https://github.com/tigeroses/leetcode/blob/master/011.integerToRoman/README.md)

整数转化为罗马数字

**input** 97

**output** 'XCVII'

[012.romanToInteger](https://github.com/tigeroses/leetcode/blob/master/012.romanToInteger/README.md)

罗马数字转整数

**input** 'XCVII'

**output** 97

[013.longestCommPrefix](https://github.com/tigeroses/leetcode/blob/master/013.longestCommPrefix/README.md)

查找字符串数组的最长公共前缀

**input** ['abc', 'abd']

**output** 'ab'

[014.3sum](https://github.com/tigeroses/leetcode/blob/master/014.3sum/README.md)

找出数组中三个数相加为0的所有组合

**input** [-2,-1,0,1,1,2,3]

**output** [[-2,0,2], [-1,0,1], [-2,-1,3], [-2,1,1]]

[015.threeSumCloset](https://github.com/tigeroses/leetcode/blob/master/015.threeSumCloset/README.md)

找出数组中三个数相加最接近某个数的结果

**input** [-1,2,1,-4]  1

**output** -1+1+2 = 2

[016.letterCombinations](https://github.com/tigeroses/leetcode/blob/master/016.letterCombinations/README.md)

计算手机数字键盘的字符组合

**input** '23'

**output** ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
