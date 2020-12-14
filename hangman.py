import random

# Store a list (or tuple) of 5 to 10 words in your script.
words = ["lemon", "orange", "mango", "lime", "peach", "pear", "grape", "plum"]

# Randomly choose a word from this list as the secret word.
secret_word = random.choice(words)
guess_count = 6

# Display the unrevealed word as underscores (with the same length.)
guess_word = "_ " * len(secret_word)
print(secret_word)
guess_list = guess_word.strip().split(" ")

print('=======================')
print('= Welcome to Hangman! =')
print('=======================')

print('_____')
print('|    |')
print('|    ')
print('|')
print('|')
print('|')
# Prompt the user to enter a letter.
while guess_count > 0:
    if secret_word == guess_word.replace(" ", ""):
        print("=========================================")
        print("= You won? Dang it.. oh I mean congrats =")
        print("=========================================")
        break

    print("Your secret word: " + guess_word)
    guess = input("Guess a letter: ")

    # If the letter is in the word, mark it as revealed and visually display that letter in the word.
    if guess in secret_word:
        print(secret_word.count(guess))
        guess_pos = secret_word.index(guess)
        # print(secret_word.index(guess))

        guess_list[guess_pos] = guess
        # print(guess_list)

        guess_word = ' '.join(guess_list)
        print('You are correct. And also lucky.')
    else:
        guess_count -= 1

        print('WRONG! BAHAHAHA')

    # If the letter is incorrect, draw another part onto the stick person.
    if guess_count == 0:
        print('_____')
        print('|    |')
        print('|    0')
        print('|   /|l')
        print('|   / l')
        print('|')
        print("=========================================")
        print("= Game over! Sucks to be a loser huh :/ =")
        print("=========================================")

    # Will display hangman
    if guess_count == 5:
        print('_____')
        print('|    |')
        print('|    0')
        print('|    ')
        print('|')
        print('|')
    if guess_count == 4:
        print('_____')
        print('|    |')
        print('|    0')
        print('|    |')
        print('|')
        print('|')
    if guess_count == 3:
        print('_____')
        print('|    |')
        print('|    0')
        print('|   /|')
        print('|')
        print('|')
    if guess_count == 2:
        print('_____')
        print('|    |')
        print('|    0')
        print('|   /|l')
        print('|    ')
        print('|')
    if guess_count == 1:
        print('_____')
        print('|    |')
        print('|    0')
        print('|   /|l')
        print('|   / ')
        print('|')
