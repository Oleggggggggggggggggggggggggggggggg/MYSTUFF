#write function reverse even
# make it reverse even numbers in a list
#e.g [1, 2, 3, 4, 5, 6,] to [1, 6, 3, 4, 5, 2]
hello = [1, 5, 4, 6, 8, 5]
def reverse_even(list1):
    dict = {}
    list2 = []
    list3 = []
    #separates numbers by substituting none for even numbers so that the indexes are normal
    for i in range(len(list1)):
        if list1[i] % 2 == 1:
            list2.append(list1[i])
        else:
            list2.append(None)
    #Takes all the even numbers and saves them in a dictionary with indexes
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            dict[i] = list1[i]
    #reverses all the even numbers and inserts them with regular indexes
    key_list = list(dict.keys())[::-1]
    value_list = list(dict.values())
    for i in range(len(key_list)):
        list2.insert(key_list[i], value_list[i])
    list3 = list2
    print(list2)
    #gets rid of all the None values
    for i in range(len(list2) - 1, -1, -1):
        if list2[i] is None:
            list3.pop(i)
    print(list3)
reverse_even(hello)