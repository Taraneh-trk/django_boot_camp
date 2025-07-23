s = input()
ext = s[s.index('.'):]
if len(ext)==4:
    print('Ok')
else:
    print('Warning')