

def snake_cafe():

    # Prints out menu
    print("**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**                                  **\n** To quit at any time, type \"quit\" **\n**************************************\n\nAppetizers\n----------\nWings\nCookies\nSpring Rolls\n\nEntrees\n----------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\nPie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears\n\n***********************************\n** What would you like to order? **\n***********************************")

    # hardcode of menu
    menu = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0, 'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0,
            'A Literal Garden': 0, 'Ice Cream': 0, 'Cake': 0, 'Pie': 0, 'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}

    while True:
        order = input('> ').capitalize()
        if order == 'Quit':
            break
        elif order not in menu:
            menu[order] = 0
            print(f"Sorry {order} is not on our menu")
            continue
        menu[order] += 1
        print(f"**{menu[order]} order of {order} have been added to your meal")


snake_cafe()
