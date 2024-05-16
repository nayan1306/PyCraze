import word_list
from hangman_art import hangman_logo, stages

# Generate a random word
word = word_list.random_word()

print(hangman_logo)

# Convert the word to a list of letters
letters = list(word)
len_letters = len(letters)

# Create a list to store guessed letters
guess_list = ['_' for _ in letters]

# Set initial lives
lives = 6
hang = False

while not hang:
    # Display the current state of the guessed word
    print(' '.join(guess_list))
    
    # Prompt the user for a guess
    choice = input("Enter your guess : ")
    
    # Check if the user wants to quit
    if choice == "quit":
        break
    
    # Check if the guessed letter is in the word
    for i in range(len_letters):
        if letters[i] == choice:
            guess_list[i] = choice
    
    # Check if all letters have been guessed
    if guess_list == letters:
        print(f"Correct Guess \n The Word was : {' '.join(guess_list)}")
        break

    # Display the current state of the guessed word after the update
    print(' '.join(guess_list))
    
    # Decrement lives if the guessed letter is not in the word
    if choice not in letters:
        print(f"You guessed {choice}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            hang = True
            print("You lose.")

    # Display hangman stages
    print(stages[lives])
