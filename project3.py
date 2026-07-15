from discount2 import discount
import random


main_dish = {
    1: ['Ayam Bakar Set', 5.80],
    2: ['Dori Bakar Set', 5.90],
    3: ['Ayam Bakar Set (Boneless)', 6.30],
    4: ['Gulai Ayam Set', 6.20],
    5: ['Ayam Penyet Set', 5.80],
    6: ['Dori Penyet Set', 5.90],
    7: ['Ayam Penyet Set (Boneless)', 6.30],
    8: ['Ayam Penyet Set (Chicken Wing)', 5.60]
}

add_on = {1: ['Rice', 0.5],
          2: ['Egg', 0.8],
          3: ['Chili', 0.5],
          4: ['Fried/Grilled Dori Fish', 3.50],
          5: ['Fried/Grilled Chicken Leg', 3.50],
          6: ['Fried/Grilled Chicken Wing', 1.50]}

shopping_cart = []

student_ids = ('000000W','261596Y','123456A','987654C','101010V','252525Z','969696R','111111Q','454545J','878787T','999999B','323232L','444444P')
staff_ids = ('STA123','STA124','STA125','STA001','STA002','STA003','STA004','STA005','STA006','STA007','STA008','STA009','STA010')



def student_or_staff():
    id = input('Enter your student/staff ID. Leave blank if member of public: ').strip().upper()
    while True:
        if id in student_ids:
            return 'student'
        elif id in staff_ids:
            return 'staff'
        elif id == '':
            return None
        else:
            print('ID not found!')


def print_menu(menu, header):
    print('=' * 45)
    print(f'{header:^40}')
    print('=' * 45)
    print(f"{'SN':<5}{'Description':<33}{'Price ($)':<35}")
    for key, value in menu.items():
        print(f'{key:<5}', end='')
        for item in value:
            print(f'{item:<35}', end='')
        print()


def add_to_cart(menu, msg):
    dish_SN = int(input(f'Select a {msg} dish SN: '))
    dish_qty = int(input('Enter the quantity required: '))
    cart = menu[dish_SN].copy()
    cart.append(dish_qty)
    shopping_cart.append(cart)


def del_from_cart():
    cart_SN = int(input(f'Select the dish SN to be deleted: '))
    del_item = shopping_cart[cart_SN - 1]
    confirm = input(f'Confirm delete {del_item[0]}? (y/n) ')
    if confirm == 'y':
        shopping_cart.pop(cart_SN - 1)


def modify_cart():
    cart_SN = int(input(f'Select the dish SN to be changed qty: '))
    change_item = shopping_cart[cart_SN - 1]
    qty = int(input(f'Enter the new quantity required for {change_item[0]}: '))
    shopping_cart[cart_SN - 1][2] = qty


def print_shopping_cart():
    print('=' * 80)
    print(f'{"Your Ordered Items":^80}')
    print('=' * 80)
    print(f"{'SN':<5}{'Ordered Items':<33}{'Price ($)':^15}{'Qty':^12}{'Sub-total($)':>10}")
    for sn, order in enumerate(shopping_cart):
        print(f'{sn + 1:<5}{order[0]:<33}{order[1]:^15}{order[2]:^12}{order[1] * order[2]:>10.1f}')
    

def take_order():

    while True:
        print_menu(main_dish, 'Penyet & BBQ Set Menu')
        add_to_cart(main_dish, 'main')

        while True:
            another_addon = input('Would you like to order an add-on? (y/n): ').strip().lower()
            if another_addon == 'y':
                print_menu(add_on, 'Add On Menu')
                add_to_cart(add_on, 'add-on')
            elif another_addon == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        continue_order = input('\nContinue ordering more main sets? (y/n): ').strip().lower()
        if continue_order == 'n':
            break

def final_receipt(group):
    total = 0
    for sn, order in enumerate(shopping_cart):
        total += order[1] * order[2]
    print('\n'*3)
    print_shopping_cart()
    discount(total,group)


def main():
    take_order()
    print_shopping_cart()
    queue = 0


    while True:
        action = input('\nWould you like to (a)dd items, (m)odify qty, (d)elete an item, or (f)inish? ').strip().lower()

        if action == 'a':
            add_choice = input("Do you want to add a (m)ain set or an (a)dd-on? ").strip().lower()

            if add_choice == 'm':
                print_menu(main_dish, 'Penyet & BBQ Set Menu')
                add_to_cart(main_dish, 'main')
                print_shopping_cart()
            elif add_choice == 'a':
                print_menu(add_on, 'Add On Menu')
                add_to_cart(add_on, 'add-on')
                print_shopping_cart()
            else:
                print("Invalid choice. Returning to the main options panel.")

        elif action == 'm':
            if len(shopping_cart) == 0:
                print("Your cart is empty!")
                continue
            modify_cart()
            print_shopping_cart()

        elif action == 'd':
            if len(shopping_cart) == 0:
                print("Your cart is empty!")
                continue
            del_from_cart()
            print_shopping_cart()

        elif action == 'f':
            group = student_or_staff()
            final_receipt(group)
            print("\nThank you for ordering! Order finalised.")
            break

        else:
            print("Invalid option. Please enter 'a', 'm', 'd', or 'f'.")




if __name__ == '__main__':
    main()
