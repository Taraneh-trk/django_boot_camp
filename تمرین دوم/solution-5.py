n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))


def minimize_difference(n, difficulties):
    total_sum = sum(difficulties)
    max_sum = total_sum

    dp = [False] * (max_sum + 1)
    dp[0] = True 

    for difficulty in difficulties:
        for i in range(max_sum, difficulty - 1, -1):
            dp[i] |= dp[i - difficulty]

    min_diff = float('inf')

    for i in range(max_sum + 1):
        if dp[i]:
            min_diff = min(min_diff, abs(i - 2 * (total_sum - i)))

    return min_diff

result = minimize_difference(n, lst)
print(result)



# def sub(lst):
#     l = []
#     for i in range(len(lst)):
#         for j in range(i,len(lst)):
#             if lst[i:j] not in l:
#                 l.append(lst[i:j])
#     return l

# lst.sort()
# sub1 = sub(lst)
# mini = sum(lst)
# for i in sub1:
#     a = []
#     for j in lst:
#         if j not in i:
#             a.append(j)
#     if 0<=sum(a)-2*sum(i)<=mini:
#         mini = sum(a)-2*sum(i)
#     if 0<=sum(i)-2*sum(a)<=mini:
#         mini = sum(i)-2*sum(a)
# print(mini)