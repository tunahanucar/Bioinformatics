str1 = input()
a = int(input())
b = int(input())
c = int(input())
d = int(input())


str2 = ""
str3 = ""
for i in range(a,b+1):
    str2 += str1[i]
for j in range(c,d+1):
    str3 += str1[j]

print(f"{str2} {str3}")

