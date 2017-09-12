# Given an array of ints, can you divide the ints into two groups, so that the sums of the two groups are the same


def split_array(li):
    small_to_big = sorted(li)
    new_li = []
    for ind, num in enumerate(small_to_big):
        if ind % 2 == 0:
            new_li.append(num)
        else:
            new_li.insert(0,num)
    mid = round(len(new_li)/2) - 1
    cumsum1 = 0
    cumsum2 = 0
    for index, numb in enumerate(new_li):
        if index <= mid:
            cumsum1 += numb
        else:
            cumsum2 += numb
    if cumsum1 == cumsum2:
        return True
    else:
        return False

print(splitArray([5,2,3]))