l =list()
l = input().split()
l2 = sorted(l,reverse =True)

print(l2)
n = len(l2)-1
min = int(l2[0])-int(l2[1])
i=0

while i<n:
      sum = int(l2[i])-int(l2[i+1])
      if min>sum:
            min =sum
      i=i+1



print(abs(min))
