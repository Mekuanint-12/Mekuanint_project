#calculating discount amount


def calculate_discount(original_price, discount_percent):

    if discount_percent >= 20:
        discount_amount = original_price * (discount_percent / 100)
        final_price = original_price - discount_amount
        return final_price
    else:
        return original_price
print(calculate_discount(100, 25))
# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount)

if discount > 0:
    print(f"The final price after {discount}% discount is: {final_price}")
else:
    print(f"No discount applied. The price is: {original_price}")