s = input().lower()
p = set(s)
p_temp = p.copy()
for i in p_temp:
    if not i.isalpha():
        p.remove(i)
all = set('qazwsxedcrfvtgbyhnujmikolp')
if p==all:
    print('Contains all letters!')
else:
    nc = len(all-p)
    print(f'Does not contain all letters and {nc} letters are missing!')
