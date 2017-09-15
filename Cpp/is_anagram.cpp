# Is anagram?

test = list(range(1,11))
print(test)
new = map(lambda x: x**2, test)   
print(list(new))


string_li = 'abaacdf'
li = [x for x in string_li if string_li.count(x) > 1]
out = set(li)
print(out)
for i in reversed(range(1,3)):
    print(i)