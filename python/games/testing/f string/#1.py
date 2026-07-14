name = "Bob"
age = 27.4545454545455
def hello():
    return "Hello"


print(f"{hello()} My name is {name} and i am {age} years old and i am a { "Kid" if age < 10  else "Adult"}")
#print(f"{age:.2f}")
print("Hello {age}")
print(f"{age:5}")