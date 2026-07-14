def get_character():
    word = "orange"
    run = True
    while run:
        try:
           index = int(input("Index: "))
           print(word[index])
        except IndexError:
           print("NET INDEXA")
        except ValueError:
           print("NET CHISLA")
        else:
           run = False
           

    
get_character()