# Author: Mishti Gala
# Email: mishtikalpes@umass.edu
# Date: 30th October 2023

# Considerations for writing the Hangman game code:
# Implement a loop that allows a maximum of six wrong guesses, representing the body parts (2 arms, 2 legs, 1 head, and 1 torso).
# Prompt the player to input a letter as their guess. Ensure that the input is a single letter and handle any potential input errors.
# Check whether the player's guess matches any letters within the secret word. Verify if the guessed letter is present in the word or not.
# If the guessed letter is not in the secret word, increment a count to keep track of the number of wrong guesses made by the player.
# Continuously show the player's progress by revealing the correct letters in the word. This helps the player see which letters they have guessed correctly and where they fit in the secret word.
# Keep the game loop running until the player either correctly guesses all the letters in the secret word or exhausts their six allowed wrong guesses. If they guess all letters correctly, exit the loop, indicating a win; if they run out of guesses, exit the loop, indicating a loss.

# The secret word the player is trying to guess.
secretWord = "Hello"
# Keeps a track of the letters guessed by the player.
lettersGuessed = ""

# The number of turns before the player loses.
failureCount = 6

# Loop until the player has made too many failed attempts.
# Will 'break' loop if they succeed instead.
while failureCount>0:

    # Get the guessed letter from the player.
    guess = input("Enter a letter: ")

    # Check if the letter guessed is in the secret word.
    if guess in secretWord:
        # Player guessed a correct letter.
        print(f"Correct! There is one or more {guess} in the secret word.")

    else:
        #Decrements the failure count when the guessed letter is incorrect.
        failureCount -= 1
        print(f"Incorrect! There are no {guess} in the secret word. {failureCount} turn(s) left.")

    # Maintain a list of all letters guessed.
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    # Loop through each letter in the secret word.
    for letter in secretWord:
        if letter in lettersGuessed:
            # If the letter has been guessed, print it.
            print(f"{letter}", end="")
        else:
            # If the letter hasn't been guessed print an underscore.
            print("_", end="")
            wrongLetterCount += 1
    print("")

    # If there were no wrong letters, then the player won!
    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secretWord}. You won!")
        break

else:
    # If the loop completes without the player winning, they lose.
    print("Sorry, you didn't win this time. Try again!")









