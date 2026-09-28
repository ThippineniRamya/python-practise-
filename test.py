# n = int(input("Enter number of inputs: "))

# for i in range(n):
#     s = input("Enter string: ")
#     print(s.split())
n=list(map(int,input().split()))
max=0
for i in n:
    if i>max:
        max=i
print(max)