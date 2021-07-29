result=[]

class Tree:
    def __init__(self,Obj):
        self.value = Obj
        self.left = None
        self.right = None

    def insertLeft(self,newNode):

        if isinstance(newNode, Tree):
            t = newNode
        else:
            t = Tree(newNode)

        if self.left is not None:
            t.left = self.left

        self.left = t

    def insertRight(self,newNode):
        if isinstance(newNode,Tree):
            t = newNode
        else:
            t = Tree(newNode)

        if self.right is not None:
            t.right = self.right
        self.right = t

    def setval(self,obj):
        self.value = obj

    #Обратный обход дерева (в глубину)
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
        result.append(self.value)

class MathExpression:
    def __init__(self, fpexp):
        self.math_exp = fpexp
        self.items = []
        self.eTree = Tree('')
        self.items.append(self.eTree)
        self.currentTree = self.eTree

    def buildTree(self):
        for i in self.math_exp.split():
            if i == '(':
                self.currentTree.insertLeft('')
                self.items.append(self.currentTree)
                self.currentTree = self.currentTree.left
            elif i not in ['+', '-', '*', '/', ')']:
                self.currentTree.setval(int(i))
                parent = self.items.pop()
                self.currentTree = parent
            elif i in ['+', '-', '*', '/']:
                self.currentTree.setval(i)
                self.currentTree.insertRight('')
                self.items.append(self.currentTree)
                self.currentTree = self.currentTree.right
            elif i == ')':
                self.currentTree = self.items.pop()
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
                arr = arr[:i - 2] + [temp] + arr[i + 1:]
                print(arr)
                i -= 2
            i += 1

        print('Result:' + str(arr[0]))

example1 = "( ( 10 - 5 ) * 3 )"
example2 = "( 3 + ( 4 * 5 ) )"

obj1 = MathExpression(example1)
obj1.getTree()
print(result)
obj1.getResultOfExpression(result)
result.clear()


