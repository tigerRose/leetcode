## 实现atoi函数

### 问题描述

实现atoi函数，将字符串转换为整型

**Input** '123'

**Output** 123

**Input** '  -123cd'

**Output** -123

### 个人思路

思路很简单，遍历字符串,首先找到第一个不为空的位置，判断符号，接下来判断是不是‘0’-‘9’，是则加入结果中，否则遍历结束

一些规则要遵守
- 数字出现前的空格要去掉
- 数字之后的其它字符全部去掉，如果数字出现前有特殊字符，直接返回0
- 超出范围-2^31 ~ 2^31-1 则返回边界值
