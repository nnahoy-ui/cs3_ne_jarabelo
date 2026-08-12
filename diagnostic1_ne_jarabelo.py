print("input cart total:")
cart_total = float(input())

print("input shipping speed (express/overnight/standard):")
shipping_speed = input()

def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 20
    elif shipping_speed == "overnight":
        shipping = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping = 0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping = 10
    else:
        print("Error")
        shipping = 0
    total = cart_total + shipping
    return total

total = calculate_checkout(cart_total, shipping_speed)
print(total)


   
          