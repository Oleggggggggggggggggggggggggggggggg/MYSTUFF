def func_new(num):
    def square(number):
        return number * number
    print(f"The answer is {square(num)}")

func_new(5)