import random
import os

word_list = ['hipnotized', 'soup', 'orgy', 'buffalo', 'space', 'miracle', 'douchebag']


def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def draw_hangman(incorrect_guesses):
    hangman_pics = [
        ''' 
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        =========
        '''
    ]
    print(hangman_pics[incorrect_guesses])

def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        os.system('cls' if os.name == 'nt' else 'clear')  
        draw_hangman(incorrect_guesses)
        print(f"\nWord: {display_word(word, guessed_letters)}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
            print("Invalid or repeated guess.")
            input("Press Enter to continue...")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word.")

        if display_word(word, guessed_letters) == word:
            print(f"\nCongratulations! You guessed the word: {word}")
            break

        input("Press Enter to continue...")

    if incorrect_guesses == max_incorrect_guesses:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_hangman(incorrect_guesses)
        print(f"\nOut of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
