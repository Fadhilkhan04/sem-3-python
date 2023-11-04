#generating a bill
def bill(p,pf,cd):
    p_price,pf_price,cd_price = 100,20,10
    total = (p_price*p) + (pf_price*pf) + (cd_price*cd)
    print("BILL :")
    print(f"Pizzas :{p}x{p_price}= Rs.{p*p_price}")
    print(f"Puffs :{pf}x{pf_price}= Rs.{pf*pf_price}")
    print(f"cool drinks :{cd}x{cd_price}= Rs.{cd*cd_price}")
    print("___________________________________________________")
    print(f"Total : Rs.{total}")

# main area

p = int(input("Quantity of pizzas :"))
pf = int(input("Quantity of puffs :"))
cd = int(input("Quantity of cool drinks :"))

bill (p,pf,cd)