def find_wizard(people, index):
    if people == []:
        return "FALSEEE"
    if people[index] == "wizard":
        return index
    return find_wizard(people, index + 1)

print(find_wizard(["farmer", "peasant", "blacksmith", "wizard", "guard"], 0))

