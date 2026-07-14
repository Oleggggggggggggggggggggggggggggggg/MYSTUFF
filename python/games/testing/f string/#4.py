def receipt():
    item = str(input("Item: "))
    price = input("Price: ")
    quantity = int(input("Quantity: "))
    print(f"Item: {item}\nPrice: {float(price):.2f}\nQuantity: {quantity}\n Total: {(quantity*float(price)):.2f}")

receipt()