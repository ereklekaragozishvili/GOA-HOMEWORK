list = []
even = []
odd = []
for i in range(10):
    numbers = int(input("enter number: "))
    list.append(numbers)
    
for i in range(len(list)):
    print(list[i])    
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("This is an even number: ",even)
print("This is an odd number: ",odd)