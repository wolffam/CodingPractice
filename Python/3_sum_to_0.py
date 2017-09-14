# Return a tuple of 3 numbers from the given list that sum to 0


def sum_to_0_dumb(in_list):
    for i in range(len(in_list)):
        for j in range(1,len(in_list)):
            for k in range(2,len(in_list)):
                if in_list[i] + in_list[j] + in_list[k] == 0:
                    print('Found one!!!')
                    return in_list[i], in_list[j], in_list[k]


# Smart implementation after sorting
def sum_to_0_sorted(li):
    li = sorted(li)
    for i in range(len(li)-2):
        j = i + 1
        k = len(li) - 1
        while j < k:
            if (li[i] + li[j] + li[k]) > 0:
                k -= 1
            elif (li[i] + li[j] + li[k]) < 0:
                j += 1
            else:
                print('Found one!!!')
                return li[i], li[j], li[k]


print(sum_to_0_dumb([-5,1,3,5,0]))

print(sum_to_0_sorted([-5,1,3,5,0]))
