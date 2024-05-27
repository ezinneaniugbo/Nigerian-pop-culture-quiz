print("Welcome to my nigerian pop culture quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("okay! let's play :)")
score = 0

answer = input("""What is the name of the award show that celebrates Nigerian music and entertainment, often referred to as the "Nigerian Grammys"? """)
if answer.lower() == "the headies":
    print("Oshey! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("""Who is known as the "Queen of Afrobeats"? """)
if answer.lower() == "tiwa savage":
    print("That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the name of the popular Nigerian reality TV show that features housemates competing for a grand prize? ")
if answer.lower() == "big brother naija":
    print("Boss! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("""Which Nigerian artist is known for the hit song "Ojuelegba"? """)
if answer.lower() == "wizkid":
    print("That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the title of Ayra Starr's debut studio album released in 2021? ")
if answer.lower() == "19 & dangerous":
    print("Oshey! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which record label is Ayra Starr signed to? ")
if answer.lower() == "mavin records":
    print("Boss! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the name of Odumodublvck's popular single released in 2021 that features a mix of Afrobeats and hip-hop? ")
if answer.lower() == "picanto":
    print("Oshey! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("""Which Nigerian female artist gained popularity with her song "Beautifully"? """)
if answer.lower() == "fave":
    print("That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("""Which Nigerian artist is known for his unique stage name "Odumodublvck"? """)
if answer.lower() == "tochukwu":
    print("Oshey! That's correct")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the title of Burna Boy's Grammy-winning album released in 2020? ")
if answer.lower() == "twice as tall":
    print("Oshey! That's correct")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")