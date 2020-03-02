def pw(n):
    f=1
    while n!=1:
        rem = n%2
        
        if rem!=0:
            f =0
            break

        n=n//2

    if f==1:
        return True
    else:
        return False


n = input()
n = int(n)
print(pw(n))
