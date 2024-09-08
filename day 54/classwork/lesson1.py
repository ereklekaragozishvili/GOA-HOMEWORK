# 1) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და დააბრუნებს მათ ჯამს
def if_positive():
  a = int(input("Enter A Num: "))
  if a > 0:
    return "Positive"
  else:
    return "Negative"

resoult = if_positive()
print(resoult)