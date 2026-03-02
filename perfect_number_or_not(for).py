n=int(input())
i = 1
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
    i += 1
if sum == n:
    print("Perfect number")
else:
    print("Not perfect")