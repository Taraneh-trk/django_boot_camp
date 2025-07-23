def find(a,b,d):
    lst = [a]
    while len(lst)!=0:
        state = lst.pop(0)
        if state == b:
            return True
        for i in (d[state] if d.get(state) else []):
            lst.append(i)
    return False

n = int(input())
d = dict()
for i in range(n):
    a2b = input()
    key , lst = a2b.split('#')
    lst = lst.split('-')
    d[key] = lst
a , b  =input().split('-')
print(find(a,b,d))
