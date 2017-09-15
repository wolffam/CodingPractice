import math, time

li = [1,1,2,2,3,4,4,5,5,6,6]

left = 0.
right = float(len(li) - 1)
found = False
mid = int((left + right)/2.)
while not found:
    if mid == 0 or mid == len(li)-1 or (li[mid] != li[mid-1]) and (li[mid] != li[mid+1]):
        print('FOUND: {}'.format(li[mid]))
        found = True
    elif li[mid] == li[mid-1]:
        right = mid - 1
        mid = int((left + right)//2.)
    elif li[mid] == li[mid+1]:
        left = mid + 1
        mid = int(math.ceil(((left + right)/2.)))
    else:
        print('UNEXPECTED')