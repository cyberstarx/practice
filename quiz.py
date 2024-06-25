print("Welcome to my first project!")
print("This is a quiz, stay and play. ")

ans= input("Would you like to play? ")
if ans!= "yes":
   quit()
   print("Perfect! Let's get started :) ")

score=0

question=input("The capital of India is: ")
if question=="New Delhi":
    print("Correct!")
    score+=1
else:
    print("Incorrect :( Please pay attention to lettering as well.")

question=input("The Prime Minister of India is: ")
if question=="Narendra Modi":
    print("Correct!")
    score+=1
else:
    print("Incorrect :( Please pay attention to lettering as well.")

question=input("National bird of India is: ")
if question=="Peacock":
    print("Correct!")
    score+=1
else:
    print("Incorrect :( Please pay attention to lettering as well.")

print("You got ",  str(score)  ,"questions correct!")
print("You got ",  str((score / 3) * 100)  ,"%.")
