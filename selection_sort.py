# O(n^2) time complexity
# O(1) space complexity


def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i+1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list [min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)


selection_sort([3,2,1,6,8,5,4])