lst = [float(i) for i in input().split(' ')]
mean = sum(lst)/len(lst)
min_ = min(lst)
mox = max(lst)
sum_ = sum(lst)
print(f'{mean:.2f} {min_:.2f} {mox:.2f} {sum_:.2f}')