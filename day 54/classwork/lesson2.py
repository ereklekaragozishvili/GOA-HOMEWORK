# 2) შექმენით ფუნქცია რომელიც შეეკითხება მომხარებელს რიცხვს და დააბრუნებს ლუწია თუ კენტი
def is_positive():
  a = int(input("Enter A Num: "))
  if a % 2 == 0:
    return "Even"
  else:
    return "Odd"
