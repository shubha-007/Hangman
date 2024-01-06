import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)


user_word=[]
wrong_word=[]

chosen_word=random.choice(word_list)
chosen_word=list(chosen_word)
for i in range(len(chosen_word)):
    user_word.append("_")

lives=6

while chosen_word!=user_word:
    guess=input("Please select a letter\n").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                user_word[i]=chosen_word[i]    
    else:
        if guess in wrong_word:
            print(f"You have already guessed {guess}")
        else:
            wrong_word.append(guess)
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(f"{lives} lives remaining")
    print(user_word)
    if user_word==chosen_word:
        print("You Won")
        break
    elif lives==0:
        print("Game Over")
        print(f"Correct word is {(chosen_word)}")
        break
    
    print(stages[lives])

