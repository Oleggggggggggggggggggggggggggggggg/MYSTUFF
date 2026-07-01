def index_error():
    numbers = [10, 20, 30]
    try:
        index = int(input("Index: "))
        print(numbers[index])
    except IndexError:
        print("The index doesnt exist")
    except ValueError:
        print("A number is required")
    finally:
        print("Program Finished")


index_error()
    
