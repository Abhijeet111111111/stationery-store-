# def oct(num):
#     if num == '0' :
#         return '0'
#     n = int(num)
#     x = n%8
#     n //= 8
#     x =  str(x)
#     n = str(n)
#     return oct(n) + x
# n = input()
# print(oct(n))

# n = input()
# f = n[:len(n)//2-1:-1]
# s = n[len(n)//2-1::-1]
# s = s.capitalize()
# print(s+f)

n = int(input())
for i in range(n):
    x = ""
    for j in range(n):
        if (i==0) or (i==n-1) or (j==0) or (j==n-1):
            x += "* "
        else:
            x += "  "
    if(i==0 or i==n-1):
        print(x[:-1])
    else:
        print(x)
