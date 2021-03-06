import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # Get a random word from words list
    while "-" in word or " " in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(
            f"You have",
            lives,
            "left and you have used these letters: ",
            " ".join(used_letters),
        )

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already guessed that chracter. Please try again")
        else:
            print("Invalid chracater. Please try again.")

    if lives == 0:
        print(f"Sorry, you died. The word was", word)
    else:
        print(f"Yay! You guessed the word", word, "!!")


def main():
    while True:
        hangman()
        keep_going = input("Do yo want to play again? (y/n): ")
        if keep_going.lower() != "y":
            break


# __name__
if __name__ == "__main__":
    main()
