#  მომხმარებელი შემოიტანს რიცხვს,
# შემდეგ კი თუ რიცხვი კენტია დაამატებთ კენტებისთვის განკუთვნილ სიაში

# თუ არადა ლუწებისთვის განკუთვნილ სიაში

# დაგჭირდებათ ორი სია და append ფუნქცია


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
even = []
odd = []
for i in  numbers:
 if i % 2 == 0:
     even.append(i)
 else:
     odd.append(i)

     print(even)
     print(odd)