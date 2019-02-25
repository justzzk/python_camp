a={'string':[],'number':[],'other':[]}
c=[12,'123',56.8,'ser',[]]
for i in c:
    if type(c) is str:
        a['string'].append(i)
    elif type(c) is (int or float):
        a['number'].append(i)
    else:
        a['other'].append(i)
print(a)

for i in c:
    print(type(i))