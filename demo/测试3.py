t=[51,25,63,51,555,142,62,1,52]
len=len(t)
for a in range(len):
    for b in range(len-a-1):
        if t[b]>t[b+1]:
            t[b],t[b+1]=t[b+1],t[b]
print(t)


print(set('runoob'))