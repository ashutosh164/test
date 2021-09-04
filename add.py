num1 = float(input('Enter first: '))
op = input('Enter operator: ')
num2 = float(input('Enter second: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op == '/':
    print(num1/num2)
elif op == '*':
    print(num1*num2)
else:
    print('Invalid operator')

print('###################')

# maximum in two number
def number(num1,num2):
    if num1>=num2:
        return num1
    else:
        return num2
print('maximum number')
print(number(num1,num2))
print('##################')


maximum = max(num1,num2)
print(maximum)


