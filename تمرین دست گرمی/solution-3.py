lst = input().split(' ')
lst[0] = float(lst[0])
me1km = 0.001
me1me = 1
me1fe = 3.280
me1mi = 0.000621
if lst[1]=='me':
    m=me1me
elif lst[1]=='km':
    m=me1km
elif lst[1]=='fe':
    m=me1fe
elif lst[1]=='mi':
    m=me1mi

if lst[2]=='me':
    k=me1me
elif lst[2]=='km':
    k=me1km
elif lst[2]=='fe':
    k=me1fe
elif lst[2]=='mi':
    k=me1mi

me = lst[0]/m
ans = me*k
print(f'{ans:.6f}')