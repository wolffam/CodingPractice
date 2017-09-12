# write a program that returns a list that contains only the elements that are common between the lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common_elements(li_1, li_2):
    output_li = set([i for i in li_1 if i in li_2])
    return output_li
print(common_elements(a,b))
