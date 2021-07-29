import re

def calc(example):
    numbers = re.split('[-+*/]', example)
    print(numbers)


    signs = []
    for elem in example:
        if elem in ['+', '-', '/', '*']:
            signs.append(elem)
    print(signs)

    arrExample = []
    for i in range(0, len(numbers)):
        arrExample.append(numbers[i])
        if i < len(signs):
            arrExample.append(signs[i])
    print(arrExample)

    i = 0
    while i < len(arrExample):
        temp = 0
        flag = False
        if arrExample[i] == '*':
            flag = True
            temp = int(arrExample[i - 1]) * int(arrExample[i + 1])
        elif arrExample[i] == '/':
            flag = True
            temp = int(arrExample[i - 1]) / int(arrExample[i + 1])
        if flag:
            print(i)
            print(arrExample)
            if i + 2 < len(arrExample):
                arrExample = arrExample[:i - 1] + [temp] + arrExample[i + 2:]
            else:
                arrExample = arrExample[:i - 1] + [temp]
            print(arrExample)
            i -= 1
        i += 1
    print(arrExample)

    i = 0
    result = 0

    while i < len(arrExample):
        flag = False
        if arrExample[i] == '+':
            result += int(arrExample[i - 1]) + int(arrExample[i + 1])
            flag = True
        elif arrExample[i] == '-':
            result += int(arrExample[i - 1]) - int(arrExample[i + 1])
            flag = True
        if flag:
            i += 2
        i += 1

    print(result)


example1 = "10-5*3"
example2 = "3+4*5"
example3 = "1+2*6/4"

calc(example1)
print('/////////////////////////')
calc(example2)
print('/////////////////////////')
calc(example3)