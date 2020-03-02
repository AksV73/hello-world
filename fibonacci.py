def fibo(n):
    n1 = 0
    n2 = 1
    print(n2,end=" ")
    while n2<int(n):
        nt = n1+n2
        n1 =n2
        n2 =nt
        print(nt,end=" ")


n = input()
fibo(n)
