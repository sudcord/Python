import random

mans = ["""
   +---+
   |   |
       |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""]

while True:
    print(("-" * 30) + "\nHangy\n" + ("-" * 30))
    
    benten = random.choice(["sudkostik" , "eren" , "adam" , "yumusakg"])
    omnitrix = 0
    yasasinirkimiz = []
    
    while True:
        print(mans[omnitrix])
        
        for i, char in enumerate(benten):
            print(char if i in yasasinirkimiz else "_"), # LESSS GOOOOOOOOO
            
        answer = raw_input("\nHey, answer!: ")
        
        if answer == benten:
            print("You lucky thing, won?\n\n")
            break
        else:
            while True:
                rand = random.randint(0, len(benten))
                if not rand in yasasinirkimiz:
                    yasasinirkimiz.append(rand)
                    break
            
            omnitrix += 1
        
        if omnitrix >= len(mans):
            print("haha, u lose. i thought.\n\n")
            break
        
    if not "y" == raw_input("You want a play game, again? (y/n):"):
        break

    # LLOOOOOOOOOOOOOOOLLLLLLLLLLLLLLL IM SODIUM HYDROXIDE
input()