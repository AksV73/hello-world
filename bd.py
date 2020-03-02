def bind(n):
    s=''
    while n!=0:
        rem = n%2
        rem = str(rem)
        s= rem+s
        n = n//2

    return s


n = input()
n = int(n)
print(bind(n))
