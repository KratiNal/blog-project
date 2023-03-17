s = 'occurancess'
count = {}
for i in s:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1
print(count)
