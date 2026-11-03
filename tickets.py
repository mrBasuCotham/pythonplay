age = int(input("how old are you? "))

if age <12:
    print("£1")
elif age > 67:
    print("£2")
else:
    card = input("do you have a rail/card (Y/N)? ")
    if card.upper() == "Y":
        print ("£10")
    else:
        print("£20")