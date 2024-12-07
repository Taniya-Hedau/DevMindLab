print("\t\t\t\t\t\t\t\t= = = Taniya's Restuarent = = =")
print("\nA. Menu List \nB. Order \nC. Bill")
for i in range(1, 4):
    choice = input("\n\nEnter your choice: ")
    if choice=="A":
        print("Menu List \n1. Pizza     ...180/- \n2. Burger     ...200/- \n3. Noodles     ...150/- \n4. Sandwich     ...120/-")
    elif choice=="B":
        dish = int(input("What would you like to have: "))
        if dish==1:
            print("Pizza     ...180/-")
            price = 180
        elif dish==2:
            print("Burger     ...200/-")
            price = 200
        elif dish==3:
            print("Noodles     ...150/-")
            price = 150
        elif dish==4:
            print("Sandwich     ...120/-")
            price = 120
        else:
            print("Sorry! out of menu.")
        plate = int(input("How many plates will you have? "))
    elif choice=="C":
        if dish>=1:
            print("Your total : ",price * plate)
        else:
            print("Sorry! you haven't ordered yet.")
    else:
        print("Sorry! wrong choice. Please try again.")