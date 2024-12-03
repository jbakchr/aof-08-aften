def calculate_price(price, discount=0):
    return price - (price * (discount / 100))


print(calculate_price(price=100))
print(calculate_price(price=200, discount=10))
print(calculate_price(price=50, discount=25))
