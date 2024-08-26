from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)



user_bet = screen.textinput("Turtle Color", "Place your bet on a turtle - Red, Blue, Green, Black, Orange or Purple ")


turtle_colors = ["red", "blue", "green", "black", "orange", "purple"]
winning_turtle = ""
game_stop = False
X_POS = -230
Y_POS = 110
turtles = []

for i in range(6):                             
    turtle = Turtle()                           
    turtle.penup()                              
    turtle.color(turtle_colors[i])              
    turtle.shape("turtle")                      
    turtle.goto(X_POS, Y_POS)                   
    Y_POS -= 40                                 
    turtles.append(turtle)                      

if user_bet:                                    
    game_stop = False                           

while not game_stop:                            
    for turtle in turtles:
        steps = random.randint(0, 10)
        turtle.forward(steps)                   
        if turtle.xcor() > 230:                
            winning_turtle = turtle.pencolor()  
            game_stop = True                    
            break                               

if user_bet == winning_turtle:                  
    print(f"You guessed it right. The winning turtle is {winning_turtle}")
else:
    print(f"Oops, you lost. The winning turtle is {winning_turtle}")



screen.exitonclick()
