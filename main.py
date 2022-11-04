import random

num = 0
def random_number_guess():
  random_num = random.randint(0,10)
  return random_num

def difference_from_answer(guess, answer = random_number_guess()):
  guess = input("what is your guess")
  if guess>answer:
    print("too high")
  elif guess<answer:
    print("too low")
  else: print("correct")
  
  

