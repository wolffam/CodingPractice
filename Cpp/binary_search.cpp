import math, time
li = [1,2,3,4,5]
item = 5

right = len(li) - 1
left = 0
midpt = int(math.ceil((right+left)/2))
found = False
while right > left and found == False:
    midpt = int(math.ceil((right+left)/2))
    print('li[midpt] = {}'.format(li[midpt]))
    if li[midpt] == item:
        found = True
        print(li[midpt])
    elif item < li[midpt]:
        right = midpt -1
    else:
        left = midpt + 1
    print('right={}'.format(right))
    print('left={}'.format(left))
    
    time.sleep(1)