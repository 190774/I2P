vcash  = float = input("Please input value of cash: ")
vprice = float = input("Please input price of chocolate: ")
vchange = float = vcash - vprice

if vchange < 0:
    print ("Please put more money in. You are short by $", vchange)





elif change == 0:
    print ("The price of chocolate is", price, "dollars.")
    print ("The amount paid is", cash, "dollars.")
    print ("No change is given.")
else:
    print ("The price of chocolate is", price, "dollars.")
    print ("The amount paid is", cash, "dollars.")
    print ("Change due is", change, "dollars.")

    FiftyCentCoin = float =0
    OneDollarCoin = float = 0
    TwoDollarCoin = float = 0
    FiveDollarCoin = float = 0
    TenDollarCoin = float = 0

    while change > 0:
        if change >= 10:
            change = change - 10
            TenDollarCoin = TenDollarCoin + 1
        elif change >= 5:
            change = change - 5
            FiveDollarCoin = FiveDollarCoin + 1
        elif change >= 2:
            change = change - 2
            TwoDollarCoin = TwoDollarCoin + 1
        elif change >= 1:
            change = change - 1
            OneDollarCoin = OneDollarCoin + 1
        elif change >= 0.5:
            change = change - 0.5
            FiftyCentCoin = FiftyCentCoin + 1

    print ("You will recieve", TenDollarCoin, "10$ coin(s),", FiveDollarCoin, "5$ coin(s),", TwoDollarCoin, "2$ coin(s),", OneDollarCoin, "1$ coin(s), and", FiftyCentCoin, "50 cent coin(s).")
