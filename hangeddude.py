import requests
import random
import os

API_KEY = 'input your API_KEY'
BASE_URL = "https://api.wordnik.com/v4/words.json/randomWord"
PARAMS = {
    "hasDictionaryDef": "true",
    "minLength": 5,
    "maxLength": 8,
    "apiKey": API_KEY
}

def choose_word():
    try:
        
        response = requests.get(BASE_URL, params=PARAMS)
        
        if response.status_code == 200:
            word = response.json()['word']
            return word.lower()  
        else:
            print(f"Failed to fetch word. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None


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
