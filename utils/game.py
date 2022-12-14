from typing import List
import random
import re


class Hangman:
    """ Class defining the Hangman game: 
    - possible_words: attribute that contains a list of words.
    - word_to_find: attribute that contains a list of strings. Each element will be a letter of the word.
    - lives: attribute that contains the number of lives that the player still has left. It should start at 5.
    - correctly_guessed_letters: attribute that contains a list of strings where each element will be a letter guessed by the user.
    - wrongly_guessed_letters: attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the word_to_find.
    - turn_count: attribute that contain the number of turns played by the player.
    - error_count: attribute that contains the number of errors made by the player.
    - 
    """

    #Class variables
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self) -> None:
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
                #select one word from the list and breaks it into a list of letters
        self.word_to_find = list(random.choice(Hangman.possible_words).upper())
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
    
    def play(self):
        """method that asks the player to enter a letter
        """

        #print the word with missing characters
        print("Guess the word:")
        print(f"({' '.join(self.correctly_guessed_letters)})\n")

        guessed_letter = input("Guess one letter for the word: ")
        if re.match("([A-z])", guessed_letter) and len(guessed_letter)==1:
            guessed_letter = guessed_letter.upper()
            print(f"The letter entered is : {guessed_letter}\n")
            if guessed_letter in self.word_to_find:
                # find location of letter index and replace the letter suggested by user
                for i, character in enumerate(self.word_to_find):
                    if character == guessed_letter:
                        self.correctly_guessed_letters[i] = guessed_letter
            else:
                self.wrongly_guessed_letters.append(guessed_letter)
                self.error_count += 1
                self.lives -=1
        else:
            print("You did not enter a letter.\n")
            self.error_count += 1
            self.lives -=1

    def well_played(self):
        """method that will provide a game summary if game is won"""
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s)!")

    def game_over(self):
        """method that will stop the game"""
        print("------------------ \n Game Over \n ------------------\n")

    def start_game(self):
        """method that starts the game"""

        while True:
            self.play()
            self.turn_count += 1
            
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break 

            if self.lives == 0 :
                self.game_over()
                break    
