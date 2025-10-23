import random
a=random.randint(1,9)
attempt=0
max_attempt=3
while attempt<max_attempt:
    b=int(input("Guess the number:-"))
    if a==b:
     print("congratulations 🎉",b," is correct answer")        
     break
    else:
      attempt+=1
      if attempt==max_attempt:
        print("you lose💔")
      else:
        print("try again")
    
     
