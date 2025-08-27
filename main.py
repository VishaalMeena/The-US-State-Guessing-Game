import turtle
import pandas as pd

# ----------------------- Setup ----------------------- #
# Load the CSV file with state names and coordinates
data = pd.read_csv("50_states.csv")

# Setup the screen with US map as background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ----------------------- Game Variables ----------------------- #
all_states = data.state.to_list()   # List of all 50 states
guessed_states = []                 # Track correctly guessed states
correct_guess = 0                   # Counter for correct guesses

# ----------------------- Main Game Loop ----------------------- #
while True:
    # Show score in the input box title
    answer_txt = screen.textinput(
        title=f"{correct_guess}/50 States Correct",
        prompt="What's another State name? (Type 'Exit' to quit)"
    )

    # Handle case when user closes the input box
    if answer_txt is None:
        break  

    # Convert guess to title case (e.g. "texas" → "Texas")
    answer_txt = answer_txt.title()

    # Exit condition -> Save the missing states into a CSV
    if answer_txt == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the guess is correct and not guessed before
    if answer_txt in all_states and answer_txt not in guessed_states:
        # Get the row of the state from CSV
        state_data = data[data.state == answer_txt]

        # Create a turtle to write the state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_txt)

        # Update game progress
        guessed_states.append(answer_txt)
        correct_guess += 1

        # If all 50 states are guessed -> Game ends
        if correct_guess == 50:
            break
