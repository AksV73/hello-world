def fact(n):
    ft = 1
    i =1
    while i<= int(n):
        ft = ft*i
        i = i+1

    print(ft)

n = input("enter number:")
fact(n)    
