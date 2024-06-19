#  შევქმნათ სია, შემდეგ მომხმარებელს შემოვატანინოთ 10 რიცხვი, ეს 10 რიცხვი დავამატოთ სიაში, 
# შევქმნათ მეორე სია სადაც დავამტებთ წინა სიიდან ყველა ლუწ რიცხვს, 
# ასევე შევქმნათ მესამე სია სადაც დავამატებთ პირველი სიიდან ველა კენტ რიცხვს

numbers = []
for i in range(1,10 + 1):
    numbers.append(i)
even = []
odd = []
for i in numbers:
    if i %2  == 0:
        odd.append(i)
for i in numbers:
    if i %2  >0:
        even.append(i)
print(even)
print(odd)