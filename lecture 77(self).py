import random
from hangman_art import logo, stages
from hangman_words import word_list

end_of_game = False
lives_left = 6
word = random.choice(word_list)
word_hidden = []
word_lenght = len(word)

print(logo)
print(stages[6])

for letter in word:
    word_hidden += "_"

print(f"{' '.join(word_hidden)}\n")

while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(word_lenght):
        if guess == word[position]:
            word_hidden[position] = guess

    if guess not in word: 
        lives_left -= 1
        print(f"\n{guess} is wrong! You lose a life now. {lives_left} lives left.")
        print(stages[lives_left])
    
    if lives_left == 0:
        end_of_game = True
        print(f"You lose. The word was {word}.")
        
    if "_" not in word_hidden:
        end_of_game = True
        print(f"You win! The word was {word}")

    if end_of_game == False:
        print(f"\n{' '.join(word_hidden)}\n")