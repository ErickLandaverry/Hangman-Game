import random

def Welcome():
  name=input('Welcome to Hangman! What is your name?')
  print("Hello " + name + "!" + " The rules are simple, guess a letter until you can guess the correct word! keep in mind that you only have 8 strikes before you lose! good luck!")
  
Welcome()

def get_guess():
  
  
  dashes = "_ " * len(secret_word)
  guesses_left = 8
  
  
  while guesses_left > -1 and not dashes == secret_word:
    
    
    print ("Word: ",dashes)
    print (str(guesses_left) + " left")
    
    
    guess = input("Make a guess:")
    
    
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      
    
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
      
    
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
  

  else:
    print ("Congrats! You win. The word was: " + str(secret_word))
    

def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     
      
    else:
      
      result = result + cur_dash[i]
      
  return result
    
words = ["addidas", "puma", "nike", "vans", "reebok", "jordan", "asics", "converse"]

secret_word = random.choice(words)
get_guess()