ls = [4,5,2,1,3,6,7,9,8]
for i in range(1, len(ls)):
    j = i
    while ls[j-1] > ls[j] and j>0:
        ls[j-1],ls[j] = ls[j],ls[j-1]
        j -=1
print(ls)

