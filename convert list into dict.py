def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))