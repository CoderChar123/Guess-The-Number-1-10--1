import random
number = random.randint (1,10)
while True: 
  print ("Welcome To Guess The Number!")
  guess = input ("Guess A Number Between 1 And 10.")
  guess = int (guess)
  if guess < 1 or guess > 10:
    print ("Invalid Range Of Number. Please Guess Again.")
  elif  guess < number:
    print ("Your Guess Was Too Low! Please Guess Again.")
  elif  guess > number:
    print ("Your Guess Was Too High! Please Guess Again.")
  elif  guess == number:
    print ("Your Guess Was Correct! Good Job! Reload The Page Too Play Again.")
    
    break