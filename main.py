import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
#In order to work with the data from the column it makes everything easier to turn it into a list
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < len(all_states) - 1:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    #Found this method online called title() which converts the guess to Title case
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        #Select only one Item
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())


screen.exitonclick()
