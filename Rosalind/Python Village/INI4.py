a = int(input())
b = int(input())

result = 0
for i in range(a,b+1):
    if i%2 == 1:
        result += i
print(result)
