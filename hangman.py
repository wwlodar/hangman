import random
import sys

name = input("Hello, what is your name?")
print("Hi, " + name +". I think it's the best time to have some fun.")
answer = input("Do you want to play hangman? ")
if answer in ["yes", "YES", "y", "Y","Yes]:
    print("Let's go! You have to guess the word that I chose. Be careful! You can make mistake only 5 times!")
else:
    print("Maybe next time.")
    sys.exit()

# choosing a random word from the list
lines_list = open('words.txt').read().splitlines()
def get_random_word():
    for word in lines_list:
        secret_word = random.choice(lines_list)
        secret_word = secret_word.lower()
    return(secret_word)
secret_word = get_random_word()

# coding the word with stars
length_stars = len(secret_word)
def star_string():
  coded_word = ("")
  i = 0
  while i < length_stars:
    coded_word +="*"
    i +=1
  return(coded_word)

# actual guessing game
def guessing():
  chances = 5
  coded_word = star_string()
  while chances > 0 and "*" in coded_word:
    x = input("Wchich letter is in the word? ").lower()
    if x in secret_word:
        # typing the same letter twice
        if x in coded_word:
            print("You already guessed it. Try another letter.")
            chances -= 1
            if chances == 1:
                print("This is your last chance")
            else:
                print("Oopsie, you've got only " + str(chances) + " tries left.")
        # correctly guessing the letter
        else:
            print("Correct!")
            indexes = [n for n,y in enumerate(secret_word) if y == x]
            coded_word = list(coded_word)
            for index in indexes:
              coded_word[index] = x
            print(coded_word)
    # making a miastake in guessing
    else:
      print("Try again!")
      chances -= 1
      print("You can try " + str(chances) + " times more!")
  # running out of chances
  else:
      if chances == 0:
          print("\n You lose, the word was: " + secret_word)
      # winning the game
      else:
          print("\n Congratulations, you won! The word was: " + secret_word)

guessing()
