#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(node):
    lst = []
    while node.next is not None:
        lst.append(node.val)
        node = node.next
    lst.append(node.val)
    print ' '.join(map(str,lst))

def addTwoNumbers(l1, l2):
    # 1 compare two list, find the longer list
    n1 = l1
    n2 = l2
    rl = None
    rt = None
    while n1.next is not None:
        if n2.next is None:
            rl = l1
            rt = l2
            break
        n1 = n1.next
        n2 = n2.next
    if n1.next is None:
        rl = l2
        rt = l1

    # print_list(rl)
    # print_list(rt)

    # 2 add the shorter list to longer list
    rr = rl
    while rt.next is not None:
        val = rt.val + rl.val
        add_next = 0
        if val > 9:
            val = val - 10
            add_next = 1
        rl.val = val

        if rl.next is not None:
            rl = rl.next
            rl.val += add_next
        rt = rt.next

    val = rt.val + rl.val
    add_next = 0
    if val > 9:
        val = val - 10
        add_next = 1
    rl.val = val
    while rl.next is not None:
        rl = rl.next
        rl.val += add_next
        if rl.val <= 9:
            break
        rl.val -= 10
    else:
        if add_next == 1:
            rl.next = ListNode(1)

    return rr


def addTwoNumbers2(l1, l2):
    dummyHead = ListNode(0)
    p = l1
    q = l2
    curr = dummyHead
    carry = 0
    while p is not None or q is not None:
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0
        sum_val = carry + x + y
        carry = sum_val / 10
        curr.next = ListNode(sum_val % 10)
        curr = curr.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next

    if carry > 0:
        curr.next = ListNode(carry)
    return dummyHead.next



