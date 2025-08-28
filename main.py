import turtle
import pandas as pd

# Load the data from CSV
data = pd.read_csv("50_states.csv")
print(data.head())  # Debug: Check the first few rows of data

# Setup the screen
screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Game variables
guessed_states = []
all_states = data.state.to_list()
correct_guess = 0
is_game_on = True

# Main game loop
while is_game_on:
    # Ask the user for a state name
    answer_txt = screen.textinput(
        title=f"{correct_guess}/50 States Correct",
        prompt="What's another State name?"
    )

    # Format the answer (capitalize first letter)
    answer_txt = answer_txt.title()

    # Only check if not already guessed
    if answer_txt not in guessed_states:

        # If the answer is correct
        if answer_txt in data.state.values:
            # Get the row for the correct state
            state_data = data[data.state == answer_txt]

            # Create a turtle to write the state name on the map
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_txt)

            # Update progress
            guessed_states.append(answer_txt)
            correct_guess += 1

            # If all states are guessed, end the game
            if correct_guess >= 50:
                is_game_on = False

    # If the user types 'Exit'
    if answer_txt == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        # Save the missing states to a CSV file
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        is_game_on = False
