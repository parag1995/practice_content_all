

def square_numbers(n):
    for i in n:
        yield i*i

ls = square_numbers([1,2,3,4,5])
print(next(ls))
# print(next(ls))
# print(next(ls))
# print(next(ls))
# print(next(ls))
# print(next(ls))
for i in ls:
    print (i)


