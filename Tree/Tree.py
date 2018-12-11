# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序主要涉及到二叉树的一些基本操作
# 定义二叉树，初始化二叉查找树，先序、中序、后序遍历二叉树

from collections import deque #为了实现非递归的层次遍历，需要使用队列

class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

#按照元素顺序，将其初始化为一个二叉查找树
def initTree(nums):
    if not nums:
        return None
    rootNode = TreeNode(nums[0])
    for item in nums[1:]:
        currNode = TreeNode(item)
        tmpNode = rootNode
        while True:
            if item <= tmpNode.val:
                if tmpNode.left == None:
                    tmpNode.left = currNode
                    break
                else:
                    tmpNode = tmpNode.left
            else:
                if tmpNode.right == None:
                    tmpNode.right = currNode
                    break
                else:
                    tmpNode = tmpNode.right
    return rootNode

#查找元素，并返回元素所在节点
def find(item, rootNode):
    if (not rootNode) or rootNode.val == item:
        return rootNode
    elif rootNode.val > item:
        return find(item, rootNode.left)
    else:
        return find(item, rootNode.right)

#查找查找二叉树的最小节点,并返回其节点位置
def findMin(rootNode):
    if (not rootNode) or (not rootNode.left):
        return rootNode
    return findMin(rootNode.left)

#查找查找二叉树的最大节点,并返回其节点位置
def findMax(rootNode):
    if (not rootNode) or (not rootNode.right):
        return rootNode
    return findMax(rootNode.right)

#向树中插入一个元素
def insert(item, rootNode):
    if (not rootNode):
        rootNode = TreeNode(item)
    elif rootNode.val > item:
        rootNode.left = insert(item, rootNode.left)
    elif rootNode.val < item:
        rootNode.right = insert(item, rootNode.right)
    else:
        pass #如果找到了相同的元素，则什么也不用做
    return rootNode

#从树中删除一个元素
def delete(item, rootNode):
    if not rootNode:
        print("Tree is Empty!") #如果不想打印，可以注释掉
        pass
    elif rootNode.val > item:
        rootNode.left = delete(item, rootNode.left)
    elif rootNode.val < item:
        rootNode.right = delete(item, rootNode.right)
    elif rootNode.left and rootNode.right: #找到目标元素且两个子节点都非空
        tmpNode = findMin(rootNode.right) #找到右子节点的最小元素
        rootNode.val = tmpNode.val
        rootNode.right = delete(tmpNode.val, rootNode.right)
    else: #左右子节点至少有一个为空
        #下面的逻辑同样可以处理没有子节点的情况
        if rootNode.left:
            rootNode = rootNode.left
        else:
            rootNode = rootNode.right
    return rootNode

#中序遍历+先序遍历，或者中序遍历+后序遍历都可以唯一确定一棵二叉树，但是先序+后序不行
#先序遍历二叉树
def preOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = preOrderScan(rootNode.left, res)
    res = res + '->' + str(rootNode.val)
    res = preOrderScan(rootNode.right, res)
    return res

#使用非递归的方式完成先序遍历
def preOrderScan2(rootNode):
    res = []
    stack = []
    while rootNode or stack:
        while rootNode:
            stack.append(rootNode) #不断地将左儿子压入栈
            rootNode = rootNode.left
        if stack:
            rootNode = stack.pop()
            res.append(rootNode.val)
            rootNode = rootNode.right #弹出栈顶元素，存储值，然后访问右儿子
    return res

def midOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = res + '->' + str(rootNode.val)
    res = midOrderScan(rootNode.left, res)
    res = midOrderScan(rootNode.right, res)
    return res

#使用非递归的方式完成中序遍历
def midOrderScan2(rootNode):
    res = [] #存储结果
    stack = [] #存储历史访问节点的栈
    while rootNode or stack:
        while rootNode:
            res.append(rootNode.val)
            stack.append(rootNode)
            rootNode = rootNode.left #不停地打印左儿子,直至为空
        if stack:
            rootNode = stack.pop().right #当前所有左儿子都打印结束后，访问右儿子
    return res

def postOrderScan(rootNode, res=''):
    if rootNode == None:
        return res + ''
    res = postOrderScan(rootNode.left, res)
    res = postOrderScan(rootNode.right, res)
    res = res + '->' + str(rootNode.val)
    return res

#使用非递归的方式完成后序遍历
def postOrderScan2(rootNode):
    if not rootNode:
        return []
    res = []
    stack = []
    stack.append(rootNode)
    pre = None #记录上一次访问的节点
    while stack:
        #查看栈顶元素
        rootNode = stack[-1]
        #如果栈顶元素的左右儿子均为空，则可以访问；如果上一次访问的节点非空且为栈顶元素的左儿子或者右儿子，那么也可以访问
        if (rootNode.left is None and rootNode.right is None) or (pre is not None and (pre == rootNode.left or pre == rootNode.right)):
            res.append(rootNode.val)
            pre = stack.pop() #访问栈顶元素并弹出
        else:
            #如果栈顶元素不能访问，那么先将右儿子压入栈，再将左儿子压入栈！！注意先后顺序，因为日后要保证先访问左儿子才能访问右儿子！
            if rootNode.right:
                stack.append(rootNode.right)
            if rootNode.left:
                stack.append(rootNode.left)
    return res

#使用非递归的方式实现层次遍历
def levelOrderScan(rootNode):
    if not rootNode:
        return []
    res = []
    queue = deque()
    queue.append(rootNode)
    while queue:
        #弹出队首元素
        rootNode = queue.popleft()
        #将左右儿子压入队尾
        if rootNode.left:
            queue.append(rootNode.left)
        if rootNode.right:
            queue.append(rootNode.right)
        res.append(rootNode.val)
    return res

def treeScan(rootNode):
    print("先序遍历")
    print(preOrderScan(rootNode))
    print("中序遍历")
    print(midOrderScan(rootNode))
    print("后序遍历")
    print(postOrderScan(rootNode))

if __name__ == "__main__":
    nums1 = [5,3,8,1,4,6,9,0,2,7,10]
    nums1 = []
    print(nums1)
    rootNode1 = initTree(nums1)
    treeScan(rootNode1)
    print(preOrderScan2(rootNode1))
    print(midOrderScan2(rootNode1))
    print(postOrderScan2(rootNode1))
    print(levelOrderScan(rootNode1))
