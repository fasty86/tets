import random

arr = [i for i in range(50)]
arr.sort()


def binary_search(start, end, lst, val):
    length = (start + end) // 2
    print(f'{length=}  {val=} {lst[length]=}')
    if val == lst[length]:
        print('GGGGGGG')
        return length
    elif val < lst[length]:
        # new = lst[:length]
        # print(new)
        return binary_search(start, length, lst, val)
    elif val > lst[length]:
        # new = lst[-length:]
        # print(new)
        return binary_search(start=length, end=end, lst=lst, val=val)

arr2 = [ 2, 3, 4, 10, 40 ]
result = binary_search(0, len(arr2)-1, arr2, 10)
print(arr)
# print(arr.index('10'))
print(f'Finded at  {result}')
