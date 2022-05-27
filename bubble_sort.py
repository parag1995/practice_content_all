def bubble_sort(custom_ls):
    for i in range(len(custom_ls)-1):
        for j in range(len(custom_ls)-i-1):
            if custom_ls[j]>custom_ls[j+1]:
                custom_ls[j], custom_ls[j+1] = custom_ls[j+1], custom_ls[j]
    print(custom_ls)

bubble_sort([3,2,5,8,6,1])