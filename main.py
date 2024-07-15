from turtle import Turtle, Screen
import pandas

#Screen Setup

screen = Screen()
screen.setup(725, 491)
screen.bgpic("US states.png")
screen.title("US States Guessing")

# For text on screen

text = Turtle()
text.penup()
text.hideturtle()

# Using Pandas for data manipulation

data_file = pandas.read_csv("50_states.csv")
total_states = data_file.state
states_guessed = []
states_to_learn = []

# Game Setup


while len(states_guessed) < 50:
    answer = screen.textinput(f"{len(states_guessed)}/50  correct",
                              "Whats another state/city name ?").title()
    if answer.title() == "Exit":
        break
    for state in total_states:
        if answer == state:
            xcor = data_file.x[data_file.state == answer]
            ycor = data_file.y[data_file.state == answer]
            text.goto(int(xcor), int(ycor))
            text.color("black")
            text.write(f"{answer}", False, "left", ("Arial", 10, "normal"))
            states_guessed.append(answer)
            break

# Creating a Dictionary of states which were not guessed

for state in total_states:
    if state not in states_guessed:
        states_to_learn.append(state)
States_dict = {
    "States to learn": states_to_learn
}

# Creating Csv file

data = pandas.DataFrame(States_dict)
data.to_csv("States to learn.csv")





