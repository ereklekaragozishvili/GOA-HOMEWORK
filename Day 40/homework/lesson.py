num1 = int(input('enter number :  '))
num2 = int(input('enter number : '))
num3 = int(input('enter number : '))
list = []
list.append(num1)
list.append(num2)
list.append(num3)

sum = 0
for i in list:
    if i > 9:
        sum += 1
print(sum)