import random
from words import word_list
from hangman_arts import stages, logo

print(logo)

chosen_word = random.choice(word_list)
#print(f'Pssst, the solution is {chosen_word}.')
display = ["_"] * len(chosen_word)

end_game = False
lifes = 6
while not end_game:
    print(*display)
    print(stages[lifes])
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess not in display:
            print(f"Nice! The letter '{guess}' exists in the word!")
            
            for index,x in enumerate(chosen_word):
                if guess == x:
                    display[index] = x
        else:
            print(f"You already guess the letter '{guess}'!")

        if "_" not in display:
            end_game = True
            print(f"Well done! The word is {chosen_word}! You win!")
    else:
        lifes -= 1
        
        if lifes == 0:
            print(stages[lifes])
            print("Oh no! You lose!")
            end_game = True
        else:
            print(f"The letter '{guess}' not exists in the word!")
    


