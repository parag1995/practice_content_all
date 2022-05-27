def merge_sort(custom_list, l, m, r):
     n1 = m-l+1
     n2 = r-m

     L = [0]*(n1)
     R = [0]*(n2)

     for i in range(0,n1):
         L[i] = custom_list[l+i]

     for j in range(0,n2):
         R[j] = custom_list(m+1+j)

     i = 0
     j = 0
     k = l
     while i<n1 and j<n2:
         if L[i] <= R[j]:
             custom_list[k] = L[i]
             i +=1
         else:
             custom_list[k] = R[j]
             j +=1
         k +=1

