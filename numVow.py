def nv(n):
    l = len(n)
    c =0
    for i in range(l):
        st = n[i]
        if st=='a'or st=='e' or st=='i' or st=='o' or st=='u':
            c+=1


    return c


n = input()
print(nv(n))           
