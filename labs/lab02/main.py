# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Dena L. 10/7/2026

# Print out title
print() # prints an empty line
print("My Awesome Quiz on Python Concepts")
print() # prints an empty line
print("* " * 20) # print a line of 20 astericks

# Ask for the user's name
print()
username = input("What is your name? ")
print(f"Hello, {username}!") # f-string format

# Ask if they want to take a quiz
print()
start_quiz = input("Do you want to take my awesome quiz? Y/N ")
if start_quiz.upper() == "Y": # this will make any lowercase input into an uppercase for comparison
    print("Great! Let's get started!")
    # put our quiz questions here all indented
    # START OUR QUIZ QUESTIONs
    
    # Set our counter to 0
    counter = 0

    # Question 1
    q1 = int(input("How would Python solve 5 * 5? "))
    if q1 == 25: # CORRECT
        # update my counter because they got the answer right
        counter += 1 # shorthand for counter = counter + 1
        print("Yes! You are correct. Python would solve this as 25.")
    else: #INCORRECT
        print("Sorry. That is not correct. ")

    # Question 2
    print()
    print(" * * * QUESTION TWO * * *")
    print("What is the function that we use to output something to the terminal?")
    print("   A - output()")
    print("   B - print()")
    print("   C - format()")
    print("   D - None of the above")
    q2 = input("Your Answer -  Choose A/B/C/D: ")
    if q2.upper() == "B":
        # update my counter because they got the answer right
        counter += 1 # shorthand for counter = counter + 1
        print("Yes! You are correct. Python would use the print() function to output something to the terminal.")
    else: #INCORRECT
        print("Sorry. That is not correct. ")

    # Question 3

    # Question 4

    # Question 5

    # Output the score
    print("* * * * YOUR FINAL SCORE * * * *")
    print(f"{username},  your final score is: {counter} out of 5.")

    # Give them feedback on their overall score
    if counter == 5:
        print("You are a rockstar! You got them all correct!")
    elif counter >= 3 and counter < 5:
        print("Great work!")
    elif counter >= 1 and counter < 3:
        print("Keep studying and try again!")
    else: 
        print("Maybe this isn't your genre? Try again later.")


elif start_quiz == "N":
    print("Sorry, maybe next time!")
    
else: # if they type anything else tell them its invalid
    print("Sorry. That is an invalid response. Try again.")

# print a farewell message
print("Thanks and have a great day!")