vprice = float (10)
vcash = float(input("Please input the money \n \n"))
vchange = float(vcash - vprice)

if vchange == 0:
    print("Thank you for the purchase")

elif vchange < 0:
    print("insufficient funds")

while vchange > 0:
   if vchange >= 10:
        print("Despensing $10")
        vchange = vchange - 10

   elif vchange >= 5:
       print ("Despensing $5")
       vchange = vchange - 5

   elif vchange >= 2:
        print("Despensing $2")
        vchange = vchange -2

   elif vchange >= 1:
        print("Despensing $1")
        vchange = vchange - 1

   elif vchange >= 0.5:
        print ("Despenisng $0.5")
        vchange = vchange - 0.5

   elif vchange <= 1:
        print ("Despenisng $0.1")
        vchange = vchange - 0.1

