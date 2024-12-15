from turtle import Turtle, Screen
import random

# Initialize a flag to indicate whether the race is on
is_race_on = False

# Create a Screen object
screen = Screen()
# Set the background color of the screen to black
screen.bgcolor("black")
# Set up the screen size (width=500, height=400)
screen.setup(width=500, height=400)

# Prompt the user to enter their bet on which turtle will win the race
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(f"user's choice {user_bet}.")

# List of colors for the turtles
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
# Corresponding y-positions for the turtles to start from
y_positions = [-100, -70, -40, -10, 20, 50, 80]

# List to hold all turtle objects
all_turtles = []

# Create and position each turtle
for turtle_index in range(0, 7):
    # Create a new turtle object
    new_turtle = Turtle(shape="turtle")
    # Set the turtle's color from the colours list
    new_turtle.color(colours[turtle_index])
    # Lift the pen to prevent drawing while moving to the starting position
    new_turtle.penup()
    # Move the turtle to the starting position
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Add the turtle to the list of all turtles
    all_turtles.append(new_turtle)

# Check if the user has made a bet
if user_bet:
    is_race_on = True

# Start the race
while is_race_on:
    # Use a for loop to move each turtle forward by a random distance
    for turtle in all_turtles:
        # Move the turtle forward by a random distance between 0 and 10
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Check if the turtle has crossed the finish line (x-coordinate greater than 220)
        if turtle.xcor() > 220:
            # Stop the race
            is_race_on = False
            # Get the color of the winning turtle
            winning_color = turtle.pencolor()
            # Check if the user's bet matches the winning turtle's color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # Exit the for loop once a turtle wins

# Exit the screen when clicked
screen.exitonclick()
