This program simulates a hangman game.

The function get_valid words takes in as a parameter a list of words. Reference words.py. Next the function picks a random word from that list. The function also checks if the word is valid beacuse some of the list has - or spaces in them. The function then returns the word in upper case.

Next within the hangman function the letters of that word are stored in a set, then it is changed to uppercase. Third an empty set called useed_letters is declared which displayes the letters the player guessed.Then the variable lives is declared to track how many chances or guesses the player has. Then a while loop is delcared which checks both how many letters of the word are left to guess and how many lives the player has left.Then the user is asked to input a guess letter. That letter is checked if it is a part of the word and if so it is displayed. Otherwise the wrong letters are displayed in using the used_letters.

Checks are perfomed if the user input has already been guessed or if its not a letter.

The while loops ends either whent the player has guessed the full word or the amount of chances falls to zero.

Added code to allow the user to either play again or quit.
