# # Importing Required Package.
import random

# Defining the function named as Code_maker which will choose the code from the list of words.
def Code_Maker():
    # Declaring a variable named as Code and assigning an empty list to it.
    Code = []
    # Initializing a for loop.
    for i in range(4):
        # Appending the random choice to the variable named as Code and returning it.
        Code.append(random.choice(['R', 'G', 'B', 'Y', 'W', 'V', 'O', 'P']))
    return Code

# Defining the function named as Feedback_Function which will give the feedback according to the user's guess.
def Feedback_Function(Code, user_guess):
    # Declaring a variable named as Feedback and assigning a list to it with two values.
    Feedback = [0, 0]
    # Initializing a for loop.
    for i in range(4):
        # Checking if the Code and the user's guess matches.
        if Code[i] == user_guess[i]:
            # If the condition is True then incrementing +1 to the 1st index of the Feedback list.
            Feedback[0] += 1

        elif Code[i] in user_guess:
            # If the condition is False then incrementing +1 to the 2nd index of the Feedback list.
            Feedback[1] += 1
    return Feedback

# Defining the function named as User_Guess_Grabber which will store the user's guesses.
def User_Guess_Grabber(number):
    # Declaring a variable named as user_guess and assigning a user input to it.
    user_guess = input("")
    # Initializing a while loop which runs if the length of the user's guess is not equal to 4 or the guess is not an alphabetic letter.
    while len(user_guess) != 4 or not user_guess.isalpha():
        # If the statement is True then declaring the same variable containing a user input with a placeholder as "Invalid". 
        user_guess = input("Invalid:  ")
    return user_guess

# Defining the function named as main which is the main branch of this process.
def main():
    # Declaring a variable named as number and assigning an integer user input to it.
    number = int(input(""))
    # Declaring a variable named as Code and calling the Code_Maker function.
    Code = Code_Maker()
    # This piece of code is used to print the answer to ensure that the program is working.
    # print(Code)
    # Initializing a for loop.
    for i in range(number):
        # Declaring a variable named as user_guess and calling the User_Guess_Grabber function with number as the parameter.
        user_guess = User_Guess_Grabber(number)
        # Printing the user's guess.
        print("g:", user_guess)
        # Declaring a variable named as Feedback and calling the Feedback_Function function with Code and user_guess as the parameters.
        Feedback = Feedback_Function(Code, user_guess)
        # Printing the Feedback.
        print("f:", Feedback)
        # Checking if the Feedback is equal to 4.
        if Feedback == [4, 0]:
            # If the condition is True then print You win and quit.
            print("You win!")
            break
    # Checking if the Feedback is not equal to 4.
    if Feedback != [4, 0]:
        # If the condition is True then print You lose! and the answer.
        print("You lose!")
        print("The Answer:",Code)

# Calling the main Function.
main()
