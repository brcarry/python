def list_len(lst):
    length = 0
    for item in lst:
        length += 1
    return length

def list_max(lst):
    if(not lst):
        return "None"
    else:
        max_num = lst[0]
        for item in lst:
            if item > max_num:
                max_num = item
        return max_num
    
def list_copy(lst):
    lst_copy = [0] * list_len(lst)
    i = 0
    for item in lst:
        lst_copy[i] = item
        i += 1
    return lst_copy


def list_append(lst, num):
    lst_append = [0] * (list_len(lst) + 1)
    i = 0
    for item in lst:
        lst_append[i] = item
        i += 1
    lst_append[i] = num
    return lst_append

def list_insert(lst, index, num):
    length = list_len(lst)
    if(index < length):
        lst_insert = [0] * (list_len(lst) + 1)
        i = 0
        for item in lst:
            if(i == index):
                lst_insert[i] = num
                i += 1
                lst_insert[i] = item
                i += 1
            else:
                lst_insert[i] = item
                i += 1
        return lst_insert           
    else:
        return list_append(lst, num)

l1 = [1,2,3]
l2 = []
print(list_len(l1))
print(list_len(l2))
print(list_max(l1))
print(list_max(l2))
print(list_copy(l1))
print(list_copy(l2))
print(list_append(l1, 7))
print(list_append(l2, 7))
print(list_insert(l1, 7, 9))
print(list_insert(l2, 7, 9))
print(list_insert(l1, 0, 11))
print(list_insert(l2, 0, 11))

