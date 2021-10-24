import random
capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def word():
    hello = ""
    running = True
    while running:
        if len(hello) == 0:
            for i in range(0, len(capital), 1):
                if capital[i] == "H":
                    hello += capital[i]
                    break
        if len(hello) == 1:
            for i in range(0, len(letters), 1):
                if letters[i] == "e":
                    hello += letters[i]
                    break
        if len(hello) == 2:  
            for i in range(0, len(letters), 1):
                if letters[i] == "l":
                    hello += letters[i]
                    break    
        if len(hello) == 3:  
            for i in range(0, len(letters), 1):
                if letters[i] == "l":
                    hello += letters[i]
                    break   
        if len(hello) == 4:  
            for i in range(0, len(letters), 1):
                if letters[i] == "o":
                    hello += letters[i]
                    hello += " "
                    break   
        if len(hello) == 6:
            for i in range(0, len(capital), 1):
                if capital[i] == "W":
                    hello += capital[i]
                    break
        if len(hello) == 7:  
            for i in range(0, len(letters), 1):
                if letters[i] == "o":
                    hello += letters[i]
                    break  
        if len(hello) == 8:  
            for i in range(0, len(letters), 1):
                if letters[i] == "r":
                    hello += letters[i]
                    break  
        if len(hello) == 9:
            for i in range(0, len(letters), 1):
                if letters[i] == "l":
                    hello += letters[i]
                    break
        if len(hello) == 10:
            for i in range(0, len(letters), 1):
                if letters[i] == "d":
                    hello += letters[i]
                    hello += "!"
                    break
        shuf = list(hello)
        random.shuffle(shuf)
        return("".join(shuf))
        
a=word()
running = True
while running:
    if a != "Hello World!":
        a = list(a)
        random.shuffle(a)
        a="".join(a)
        print(a) # 1/39916800 chance to get it right
    if a == "Hello World!":
        print(a)
        running = False


