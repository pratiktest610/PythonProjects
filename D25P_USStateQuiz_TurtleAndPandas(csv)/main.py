import turtle
import pandas
# state_list = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']


screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.bgpic(image)
found = 0
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []
missing_states = []

while found != 50:
    guess = screen.textinput(f"{found}/50 States Guessed", "Enter state's name here")

    if guess == "exit":
        break

    if guess.title() in all_states:
        guessed_states.append(guess.title())
        found += 1
        state = data[data.state == guess.title()]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state.x), int(state.y))
        tim.write(f"{guess.title()}", align="center", font=("Courier", 16, "normal"))

missing_states = [state for state in all_states if state not in guessed_states]
df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")

