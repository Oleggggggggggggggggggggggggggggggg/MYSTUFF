def fibonacci(nums):
    mylist = [0, 1]
    if nums <=2 and nums > 0:
            return mylist[:nums]
    if nums > 2:
            for i in range(2, nums):
                   mylist.append(mylist[i-1] + mylist[i-2])
            return mylist
print(fibonacci(100))