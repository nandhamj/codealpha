import random

# Word list
words = ["apple", "banana", "cherry", "date", "elderberry"]

def hangman():
    word = random.choice(words).upper()
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word is: {' '.join(guessed)}")

    while attempts > 0 and "_" in guessed:
        print(f"\nRemaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            guessed = ''.join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
            print(f"Good job! The word is now: {' '.join(guessed)}")
        else:
            attempts -= 1
            print(f"Wrong guess. The word is still: {' '.join(guessed)}")

    if "_" not in guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

hangman()
