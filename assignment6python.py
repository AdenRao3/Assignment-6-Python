# Created by: Aden Rao
# Created on: May 14, 2019
# This program lets a user enter a number in a text field and what this does is it calculates the value of pi by counting the iterations of it based on what the user entered in the text field.

# Iteration variable that is equal to what the user enters in the input
iterations = int(input("Enter a number: "))+1

# Logic variable that is used to determine pi
logic = -1

# Answer variable which starts at 0
answer = 0

# For loop used to determine the value of pi
for math in range(1, iterations, 1):
    logic = logic*-1
    answer = answer + 4/(2*math-1)*logic

# If statement to make the user has entered a postive number and if they haven't then tell to enter a postive number.
if answer > 0:
    print("The Answer Is: ", answer)
else:
    print("Please enter a positive number")

