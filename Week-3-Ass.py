def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_discounted_price = price - discount_amount
        return f'${final_discounted_price}'
    else:
        return f'''The Discount percent: ${discount_percent} is less than 20.
          Thus, the price is ${price}'''


price = float(input("Enter the item price: "))
discount_percent = float(input("Enter the discount percentage: "))

print(calculate_discount(price, discount_percent))
