while True:
    n=input("Введите количество элементов массива: ")
    try:
        n=int(n)
        break
    except ValueError:
        print('Введите (ЧИСЛО) количество элементов массива: ', end='')
        pass
A=[0]*n
max_numb=-999999999
for i in range(n):
    print('A[',i,'] = ', end='')
    while True:
        A[i]=input()
        try:
            A[i]=float(A[i])
            break
        except ValueError:
            print('Введите число в массиве A[',i,'] = ', end='')
            pass
    if A[i]>max_numb:
        max_numb=A[i]
        diff=n-i-1
for i in range(n):
    if A[i]!=max_numb:
        while diff!=0:
            A[n-1]=0
            n-=1
            diff-=1
print('Измененный массив: ',A)


