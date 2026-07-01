def square_number():
    try:
        number = int(input("NUMBER: "))
        print(number * number)
    except ValueError:
        print("NET")

square_number()
