n = int(input())

l_name = list(input().split(" "))
for i in range(n):
    sum = 0
    l = len(l_name[i])
    for j in range(l):
        a = ord(l_name[i][j])-96
        sum = sum+a
    print(sum)    