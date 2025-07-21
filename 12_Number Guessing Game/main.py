#Number Guessing Game Objectives:
from art import logo 
print(logo)
from random import randint
easy_level_turns=10
hard_level_turns=5
turns=0
def check_answer(guess,answer,turns):
  if guess > answer:
    print("Too high")
    return turns-1
  elif guess < answer:
    print("Too low")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level_turns
  else:
    return hard_level_turns
def game():  
  print("Welcome to the guessing game.")
  print("I'm thinking of a number between 1 and 100.")
  answer=randint(1,100)
  turns=set_difficulty()
  
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
  guess=0
  while guess !=answer: 
    print(f"You have {turns} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    turns=check_answer(guess,answer,turns)
    if turns==0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
      

game()
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

