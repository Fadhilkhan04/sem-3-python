#generating bill

def bill(a,b,c):
  a_price,b_price,c_price = 30,20,50
  total = a*a_price + b*b_price + c*c_price
  print(f"BILL")
  print(f"1.juice : {a}x{a_price} = Rs{a*a_price}")
  print(f"2.chips : {b}x{b_price} = Rs{b*b_price}")
  print(f"3.icecream : {c}x{c_price} = Rs{c*c_price}")
  print(f"_______________________________")
  print(f"total : Rs{total}")

#main area

a = int(input("enter the quantity of juice:"))
b = int(input("enter the quantity of chips:"))
c = int(input("enter the quantity of icecream:"))

bill(a,b,c)