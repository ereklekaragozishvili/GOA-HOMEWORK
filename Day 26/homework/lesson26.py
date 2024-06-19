# მომხმარებელს შეეკითხეთ სწავლობს თუარა გოაში,
#  თუ სწავლობს შეეკითხეთ ომელ ჯგუფშია,
# თუ პასუხი იქნება ჯგუფი13 შეეკითეთ რომ არის თუ არა გაბრიელი მისი მენტორი, 
# თუ პასუხი იქნება კი უთხარით რომ თქვენც აქ სწავლობთ და ნამდვილად გაბრიელია ორივეს მენტორი, 
# თუ პასუხი არიქნება გაბრიელი ყველა სხვა შემთხვევაში დაუბეჭდეთ რომ ის ტყუის და არარის სინამდვილეში ჯგუფ13-ში 




num1 = input("swavlob tuara goashi?" )

while num1 != "diax":
    num1 = input("swavlob tuara goashi?: ")


if num1 == "diax":
  num2 = int(input("romel jgufshi xart? : "))



if num2 == 13:
    num3 =   input("aris tuara gabrieli sheni mentori? ")



if num3 == "diax":
    input("mec aq swavlob da namdvilad gabrielia chveni mentori ")
else:
    print("tyuixar shen ar xar jguf 13-shi")