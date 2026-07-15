# price = input("Enter the original price: ")
# group = input("Are you a student or staff?: ")
#
# def calculate_discount(price, group):
#
#     if group.lower() == "student":
#         discount = 0.10  # 10%
#     elif group.lower() == "staff":
#         discount = 0.05  # 5%
#     else:
#         discount = 0.00  # No discount
#
#     final_price = price * (1 - discount)
#     return final_price






# price = float(input("Enter the original price: "))
# group = input("Are you a student or staff?: ")
#
# def calculate_discount(price, group):
#     if group.lower() == "student":
#         discount = 0.10
#     elif group.lower() == "staff":
#         discount = 0.05
#     else:
#         discount = 0.00
#
#     discount_amount = price * discount
#     final_price = price - discount_amount
#
#     return price, discount, discount_amount, final_price
# original_price, discount, discount_amount, final_price = calculate_discount(price, group)
# print(f"Original Price : ${original_price:.2f}")
# print(f"Discount       : {discount*100:.0f}%")
# print(f"You Save        : ${discount_amount:.2f}")
# print(f"Final Price    : ${final_price:.2f}")


# def student_or_staff():
#     price = float(input("Enter the original price: "))
#     group = input("Are you a student or staff?: ")
#     return price, group
#
#
# def calculate_discount(price, group):
#     if group.strip().lower() == "student":
#         discount = 0.10  # 10%
#     elif group.strip().lower() == "staff":
#         discount = 0.05  # 5%
#     else:
#         discount = 0.00  # No discount
#
#     final_price = price * (1 - discount)
#     return final_price
#
#
# price, group = student_or_staff()
# final_price = calculate_discount(price, group)
# print(f"Final price: ${final_price:.2f}")

#############################################
student_ids = 


def student_or_staff():
    price = float(input("Enter the original price: "))
    group = input("Are you a student or staff ?(y/n): ")
    return price, group


def calculate_discount(price, group):
    if group.strip().lower() == "student":
        discount = 0.10  # 10%
    elif group.strip().lower() == "staff":
        discount = 0.05  # 5%
    else:
        discount = 0.00  # No discount

    discount_amount = price * discount
    subtotal = price - discount_amount

    return price ,discount, discount_amount, subtotal

def final_payment(subtotal):
    # print(f'Subtotal: ${price:.2f}')
    #print(f'Discount: {discount}')
    gst = subtotal * 0.09
    # print(f'GST: ${gst:.2f}')
    final_price = subtotal + gst
    # print(f'Final price: ${final_price:.2f}')
    return final_price, subtotal, gst

def print_receipt():
    print('=' * 45)
    print(f'Receipt')
    print('=' * 45)
    final_payment(subtotal)


price, group = student_or_staff()
original_price, discount, discount_amount, subtotal = calculate_discount(price, group)
final_price, subtotal, gst = final_payment(subtotal)

print_receipt()
print(f"Original price: {price:.2f}")
print(f"Discount: {discount*100:.0f}%")
print(f"You saved: {discount_amount:.2f}")
print(f'GST: ${gst:.2f}')
print(f'Final price: ${final_price:.2f}')
