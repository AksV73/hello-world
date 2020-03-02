def pl(n):
    m = n[::-1]

    if m==n:
       return 1
    else:
        return 0


n = input()
print(pl(n))
