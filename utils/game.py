import numpy as np
from random import randint
import re


class hangman:
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
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
           

    def play():
        """method that asks the player to enter a letter
        """

        #select one word from the list and breaks it into a list of letters
        hangman.word_to_find = re.findall("\w",(hangman.possible_words[randint(0,len(hangman.possible_words)-1)]).upper())
        hangman.correctly_guessed_letters = [""]*len(hangman.word_to_find)

        guessed_letter = input("Guess one letter for the word: \n")
        if re.match("\w", guessed_letter):
            guessed_letter = guessed_letter.upper()
            print("The letter entered is : {guessed_letter}")
            if guessed_letter in hangman.word_to_find:
                letter_index = np.where(hangman.word_to_find == guessed_letter) # find location of letter index
                hangman.correctly_guessed_letters[letter_index] = guessed_letter # replace the letter suggested by user
                return True
            else:
                hangman.wrongly_guessed_letters.append(guessed_letter)
                hangman.error_count += 1
                hangman.lives -=1
                return False
        else:
            print("You did not enter a letter.")
            return False

    def well_played():
        """method that will provide a game summary if game is won"""
        print(f"You found the word: {hangman.word_to_find} in {hangman.turn_count} turns with {hangman.error_count} errors!")

    def game_over():
        """method that will stop the game"""
        print("------------------ \n Game Over \n ------------------\n")

    def start_game():
        """method that starts the game"""
        while(hangman.lives>0):
            hangman.play()
            hangman.turn_count += 1
            if(hangman.correctly_guessed_letters == hangman.word_to_find):
                hangman.well_played()
                return  
        
        hangman.game_over()
    
