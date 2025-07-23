lst = []
def canPartition(lst):
    total_sum = sum(lst)
    if total_sum % 2 != 0:
        return False

    subset_sum = total_sum // 2
    dp = [False] * (subset_sum + 1)
    dp[0] = True

    for num in lst:
        for i in range(subset_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[subset_sum]

if len(k:=input()) != 0:
    m = k.split(' ')
    for i in m:
        lst.append(int(i))
    if canPartition(lst):
        print("Yes")
    else:
        print("No")
else:
    print('Yes')




# def sub(lst):
#     l = []
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst) + 1):
#             subset = lst[i:j]
#             if subset not in l:
#                 l.append(subset)
#     return l

# def e(lst, sub1):
#     for i in sub1:
#         a = lst.copy()
#         for j in i:
#             a.remove(j)
#         if sum(a) == sum(i):
#             return True
#     return False


# sub1 = sub(lst)

# if e(lst, sub1):
#     print('Yes')
# else:
#     print('No')
