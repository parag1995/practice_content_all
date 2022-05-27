# O(n^2)
# O(1) space complexity

def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j>=0 and key<custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -=1
        custom_list[j+1] = key
    print(custom_list)

insertion_sort([2,1,6,3,4,8])