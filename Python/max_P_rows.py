# Given an N by M matrix of T's and P's, find the max number of all P rows given a certain number of T flips
import numpy as np


def max_P_rows(in_mat, num_t_flips):
    rows, cols = np.shape(in_mat)
    p_list = []
    for row in range(rows):
        num_p = 0
        for col in range(cols):
            if in_mat[row,col] == 'P':
                num_p += 1
        p_list.append(num_p)
    p_list = sorted(p_list, reverse = True)
    num_after_flips = 0
    for entry in p_list:
        if entry == cols:
            num_after_flips += 1
        elif entry + num_t_flips >= cols:
            num_after_flips += 1
            num_t_flips = entry + num_t_flips - cols
        else:
            break
    return num_after_flips


test_mat = np.array([['P', 'P', 'P', 'P'],
                     ['P', 'T', 'P', 'P'],
                     ['P', 'T', 'P', 'T']])
print(max_P_rows(test_mat, 0))
print(max_P_rows(test_mat, 1))
print(max_P_rows(test_mat, 2))
print(max_P_rows(test_mat, 3))
