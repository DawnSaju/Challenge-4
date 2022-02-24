# Challenge-4

### CodeBeans 1.0 - Challenge 4

- Importing Required Package.
```python
import random
```
### Code_maker

- Defining the function named as Code_maker which will choose the code from the list of words.
- Declaring a variable named as Code and assigning an empty list to it.
- Initializing a for loop.
- Appending the random choice to the variable named as Code and returning it.

```python
def Code_Maker():
    Code = []
    for i in range(4):
        Code.append(random.choice(['R', 'G', 'B', 'Y', 'W', 'V', 'O', 'P']))
    return Code
```
### Feedback_Function

- Defining the function named as Feedback_Function which will give the feedback according to the user's guess.
- Declaring a variable named as Feedback and assigning a list to it with two values.
- Initializing a for loop.
- Checking if the Code and the user's guess matches.
- If the condition is True then incrementing +1 to the 1st index of the Feedback list.
- If the condition is False then incrementing +1 to the 2nd index of the Feedback list.

```python
def Feedback_Function(Code, user_guess):
    Feedback = [0, 0]
    for i in range(4):
        if Code[i] == user_guess[i]:
            Feedback[0] += 1

        elif Code[i] in user_guess:
            Feedback[1] += 1
    return Feedback
```
### User_Guess_Grabber

- Defining the function named as User_Guess_Grabber which will store the user's guesses.
- Declaring a variable named as user_guess and assigning a user input to it.
- Initializing a while loop which runs if the length of the user's guess is not equal to 4 or the guess is not an alphabetic letter.
- If the statement is True then declaring the same variable containing a user input with a placeholder as "Invalid". 

```python
def User_Guess_Grabber(number):
    user_guess = input("")
    while len(user_guess) != 4 or not user_guess.isalpha():
        user_guess = input("Invalid:  ")
    return user_guess
```
### Main

- Defining the function named as main which is the main branch of this process.
- Declaring a variable named as number and assigning an integer user input to it.
- Declaring a variable named as number and assigning an integer user input to it.
- This piece of code is used to print the answer to ensure that the program is working.
- Initializing a for loop.
- Declaring a variable named as user_guess and calling the User_Guess_Grabber function with number as the parameter.
- Printing the user's guess.
- Declaring a variable named as Feedback and calling the Feedback_Function function with Code and user_guess as the parameters.
- Printing the Feedback.
- Checking if the Feedback is equal to 4.
- If the condition is True then print You win and quit.
- Checking if the Feedback is not equal to 4.
- If the condition is True then print You lose! and the answer.
- Calling the main Function.

```python
def main():
    number = int(input(""))
    Code = Code_Maker()
    # print(Code)
    for i in range(number):
        user_guess = User_Guess_Grabber(number)
        print("g:", user_guess)
        Feedback = Feedback_Function(Code, user_guess)
        print("f:", Feedback)
        if Feedback == [4, 0]:
            print("You win!")
            break
    if Feedback != [4, 0]:
        print("You lose!")
        print("The Answer:",Code)
```

- Calling the main Function.
```python
main()
```
