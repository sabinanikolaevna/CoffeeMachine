water = 400
milk = 540
beans = 120
cups = 9
money = 550
while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == 'remaining':
        print("The coffee machine has:")
        print(str(water) + " ml of water")
        print(str(milk) + "  ml of milk")
        print(str(beans) + " g of coffee beans")
        print(str(cups) + " disposable cups")
        print("$" + str(money) + " of money")
    elif action == 'buy':
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if order == '1':
            if water < 250 or beans < 16 or cups < 1:
                print("Sorry, not enough water!")
            else:
                water -= 250
                milk -= 0
                beans -= 16
                cups -= 1
                money += 4
                print("I have enough resources, making you a coffee!")
        elif order == '2':
            if water < 350 or milk < 75 or beans < 20 or cups < 1:
                print("Sorry, not enough water!")
            else:
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
                print("I have enough resources, making you a coffee!")
        elif order == '3':
            if water < 200 or milk < 100 or beans < 12 or cups < 1:
                print("Sorry, not enough water!")
            else:
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
                print("I have enough resources, making you a coffee!")
    elif action == 'back':
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    elif action == 'fill':
            addwater = input("Write how many ml of water you want to add:")
            addmilk = input("Write how many ml of milk you want to add:")
            addbeans = input("Write how many grams of coffee beans you want to add:")
            addcups = input("Write how many disposable cups of coffee you want to add:")
            water += int(addwater) 
            milk += int(addmilk)
            beans += int(addbeans)
            cups += int(addcups)
    elif action == 'take':
        print("I gave you $" +str(money))
        money = 0
    elif action == 'exit':
        break
