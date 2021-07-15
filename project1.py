print('Введите число а=')
a = int(input())

print('Введите число b=')
b = int(input())

print('Выберите операцию')
print('1 - сложить a+b')
print('2 - вычесть a-b')
d = int(input())

if d==1:
    print ('Сумма a+b=', a+b)

if d==2:
    print ('Разность a-b=', a-b)
