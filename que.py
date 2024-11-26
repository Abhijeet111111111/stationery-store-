def product_of_squares(num):
    tens = num//10
    units = num%10
    return (tens**2)*(units**2)
def find_result(num1,num2):
    product1 = product_of_squares(num1)
    product2 = product_of_squares(num2)
    difference = product1 - product2
    if difference < 0:
        return 'N'
    elif difference > 0:
        return 'P'
    else:
        return 'Z'
num1 = int(input())
num2 = int(input())
print(find_result(num1,num2))