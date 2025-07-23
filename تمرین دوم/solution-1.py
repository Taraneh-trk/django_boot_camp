n = int(input())
lst = input().strip().split(' ')
li = []
for i in range(0, len(lst) - 1, 2):
    li.append((int(lst[i]), int(lst[i + 1])))

li.sort(key=lambda x: x[1]) 

count = 0
end = 0
answer = [] 
  
for interval in li: 
    if(end <= interval[0]): 
        end = interval[1] 
        count += 1
        answer.append(interval) 

print(count) 
