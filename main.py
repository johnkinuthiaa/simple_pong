from turtle import Screen, Turtle
import time

screen = Screen()
screen.bgcolor("black")
screen.title("pong game")
screen.setup(800,600)
screen.tracer(0)


class Paddle(Turtle):
    def __init__(self, position) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid =5,stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y =self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.01
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y= self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *0.9
        
    def bounce_x(self):
        self.x_move *=-1
        self.ball_speed *0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed =0.01
        
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboad()
        
    def update_scoreboad(self):
        self.clear()
        self.goto(-200,250)
        self.write(self.l_score, align="center" , font=("Courier",20, "normal"))
        self.goto(200,250)
        self.write(self.r_score, align="center" , font=("Courier",20, "normal"))
        
        
    def l_point(self):
        self.l_score +=1
        self.update_scoreboad()
        
    def r_point(self):
        self.r_score +=1
        self.update_scoreboad()
        

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"q")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
