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
import Group10_262052Q_1
student_ids = ('000000W','261596Y','123456A','987654C','101010V','252525Z','969696R','111111Q','454545J','878787T','999999B','323232L','444444P')
staff_ids = ('STA123','STA124','STA125','STA001','STA002','STA003','STA004','STA005','STA006','STA007','STA008','STA009','STA010')



def student_or_staff():
    id = input("input your student/staff id. Leave blank or otherwise if member of public: ").strip().upper()
    if id in student_ids:
        group = 'student'
    elif id in staff_ids:
        group = 'staff'
    else:
        return None
    return group


def calculate_discount(group):
    price = float(input('Enter total price of amount: '))
    if group == "student":
        discount = 0.10  # 10%
    elif group == "staff":
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
    group = student_or_staff()
    original_price, discount, discount_amount, subtotal = calculate_discount(group)
    final_price, subtotal, gst = final_payment(subtotal)
    print(f"""

    {'=' * 45}
    Receipt
    {'=' * 45}
    Original price: {original_price:.2f}
    Discount: {discount*100:.0f}%
    You saved: {discount_amount:.2f}
    GST: ${gst:.2f}
    Final price: ${final_price:.2f}

    """)

def main():
    print_receipt()




if __name__ == '__main__':
    main()





