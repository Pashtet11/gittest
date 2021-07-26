from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree, result

class MathExpression:
    def __init__(self, fpexp):
        self.math_exp = fpexp
        self.pStack = Stack()
        self.eTree = BinaryTree('')
        self.pStack.push(self.eTree)
        self.currentTree = self.eTree

    def buildTree(self):
        for i in self.math_exp.split():
            if i == '(':
                self.currentTree.insertLeft('')
                self.pStack.push(self.currentTree)
                self.currentTree = self.currentTree.getLeftChild()
            elif i not in ['+', '-', '*', '/', ')']:
                self.currentTree.setRootVal(int(i))
                parent = self.pStack.pop()
                self.currentTree = parent
            elif i in ['+', '-', '*', '/']:
                self.currentTree.setRootVal(i)
                self.currentTree.insertRight('')
                self.pStack.push(self.currentTree)
                self.currentTree = self.currentTree.getRightChild()
            elif i == ')':
                self.currentTree = self.pStack.pop()
            else:
                raise ValueError
        return self.eTree

    def getTree(self):
        pt = self.buildTree()
        pt.postorder()

    def getResultOfExpression(self, arr):
        i = 0
        while len(arr) > 1:
            temp = 0
            flag = False
            if arr[i] == '+':
                temp = arr[i - 2] + arr[i - 1]
                flag = True
            elif arr[i] == '-':
                temp = arr[i - 2] - arr[i - 1]
                flag = True
            elif arr[i] == '*':
                temp = arr[i - 2] * arr[i - 1]
                flag = True
            elif arr[i] == '/':
                temp = arr[i - 2] / arr[i - 1]
                flag = True
            if flag:
                print(i)
                print(arr)
                arr = arr[0: i - 2] + [temp] + arr[i + 1: len(arr) + 1]
                print(arr)
                i = i - 2
            i = i + 1

        print('Результат:' + str(arr[0]))

example1 = "( ( 10 + 5 ) * 3 )"
example2 = "( 3 + ( 4 * 5 ) )"

obj1 = MathExpression(example1)
obj1.getTree()
print(result)
obj1.getResultOfExpression(result)
result.clear()

print('////////////////////////////////////////////')

obj2 = MathExpression(example2)
obj2.getTree()
print(result)
obj2.getResultOfExpression(result)
