shopping_cart = []

def get_valid_SN(menu, msg):
    while True:
        try:
            dish_SN = int(input(f'Select a {msg} dish SN:'))
            if dish_SN in menu:
                return dish_SN
            else:
                print('Invalid dish SN.')
        except ValueError:
            print(f'Please select a valid dish.')

def get_valid_qnty(menu, msg):
    while True:
        try:
            dish_qty = int(input(f'Enter quantity required:'))
            if dish_qty in menu:
                return dish_qty
            else:
                print('Invalid quantity.')
        except ValueError:
            print(f'Please enter a valid quantity.')

def add_to_cart(menu, msg):
    dish_SN = get_valid_SN(menu, msg)
    dish_qty = get_valid_qnty(menu, msg)
    cart = menu[dish_SN].copy()
    cart.append(dish_qty)
    shopping_cart.append(cart)


add_on = {1: ['Rice', 0.50],
          2: ['Egg', 0.80],
          3: ['Chili', 0.50],
          4: ['Fried/Grilled Dori Fish', 3.50],
          5: ['Fried/Grilled Chicken Leg', 3.50],
          6: ['Fried/Grilled Chicken Wing', 1.50]}



def free_add_on():
    # if final_price>10:
    while True:
        addon_option = input('Do you want a free Chicken Wing? (y/n): ')
        if addon_option == 'y':
            free_item = add_on[6].copy()
            free_item[0] = "FREE " + free_item[0]
            free_item[1] = 0.00
            free_item.append(1)
            shopping_cart.append(free_item)
            print(f'Added item to shopping cart!')
            break
        elif addon_option == 'n':
            print(f'Thank You!')
            break
        else:
            print('Invalid option.')

free_add_on()

