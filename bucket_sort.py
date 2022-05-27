import math
import insertion_sort


def bucket_sort(custom_list):
    numberofbuckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []

    for i in range(numberofbuckets):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j*numberofbuckets/max_value)
        arr[index_b-1].append(j)

    for i in range(numberofbuckets):
        arr[i] = insertion_sort.insertion_sort(arr[i])

    print(arr)

bucket_sort([2,1,3,6,4,5,9,7,8])