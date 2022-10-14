while True:
    n=input("Введите количество элементов массива: ")
    try:
        n=int(n)
        break
    except ValueError:
        print('Введите (ЧИСЛО) количество элементов массива: ', end='')
        pass
A=[0]*n
for i in range(n):
    print('A[',i,'] = ', end='')
    A[i] = input()
while True:
    n1=input("Введите количество элементов массива: ")
    try:
        n1=int(n1)
        break
    except ValueError:
        print('Введите (ЧИСЛО) количество элементов массива: ', end='')
        pass
B=[0]*n1
for j in range(n1):
    print('A[',j,'] = ', end='')
    B[j] = input()
common=[x for x in A if x in B]
print(common)


