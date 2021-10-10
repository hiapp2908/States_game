import turtle as tl
import pandas as pd

data = pd.read_csv("Indian States.csv")

state_list = data["States"].to_list()

guessed_state = []


def get_coordinates(location):
    x = int(data[data["States"] == location]["x"])
    y = int(data[data["States"] == location]["y"])
    return (x, y)


screen = tl.Screen()
screen.title("Indian States Game")
screen.setup(width=500, height=600)
image = "InSmall.gif"

screen.addshape(image)
tl.shape(image)
screen.tracer(0)

while len(guessed_state) != len(state_list):
    answer = screen.textinput(f"{len(guessed_state)}/{len(state_list)} Guess the state", "Enter the name of the state").title()
    # score = tl.Turtle()
    # score.penup()
    # score.hideturtle()
    # score.goto(x=0, y=280)
    # score.clear()
    # score.write(f"{len(guessed_state)}/{len(state_list)} Guessed", align="center", font=("Ariel", 10, "bold"))
    # screen.update()
    if answer == "Exit":
        states_to_learn = [state for state in state_list if state not in guessed_state]
        # for state in state_list:
        #     if state not in guessed_state:
        #         states_to_learn.append(state)
        print(f"Your score is {len(guessed_state)}/{len(state_list)}")
        print(f"You need to learn about these: {states_to_learn}")
        missing_states = pd.DataFrame(states_to_learn)
        missing_states.to_csv("states_to learn.csv")
        break

    if answer in state_list:
        guessed_state.append(answer)
        t = tl.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(get_coordinates(answer))
        t.write(answer, align="center")
        screen.update()

tl.mainloop()


# def get_coordinates(x, y):
#     print(x, y)
# tl.onscreenclick(get_coordinates)

