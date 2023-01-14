from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

# Set up objects and variables
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake!")
screen.tracer(0)
game = True
score = 0
high_score = 0
show_score = Turtle()
show_score.penup()
show_score.hideturtle()
show_score.color("white")
show_score.goto(x=0, y=250)
show_score.write(f"Score: {score}", align="center", font=('Arial', 24, 'bold'))
show_high_score = Turtle()
show_high_score.penup()
show_high_score.hideturtle()
show_high_score.color("white")
show_high_score.goto(x=0, y=-280)
show_high_score.write(f"High Score: {high_score}", align="center", font=('Arial', 24, 'bold'))
try_again = Turtle()
try_again.penup()
try_again.hideturtle()
try_again.color("white")
try_again.goto(x=0, y=0)
snake = Snake()
food = Food()


def play_game():
    while game:
        screen.listen()
        screen.onkey(key="w", fun=snake.move_up)
        screen.onkey(key="a", fun=snake.move_left)
        screen.onkey(key="s", fun=snake.move_down)
        screen.onkey(key="d", fun=snake.move_right)
        screen.update()
        snake.move()
        # Add delay so snake does not update infinitely fast
        time.sleep(0.1)
        snake_head = snake.get_head()

        # Call check methods
        check_food_collision(snake_head)
        check_tail_collision(snake_head)
        check_wall_collision(snake_head)
    # After game is false
    try_again.write("Press space to try again", align="center", font=('Arial', 24, 'bold'))
    screen.onkey(key="space", fun=reset_game)

# Reset game
def reset_game():
    global game, high_score, score, snake, food
    if not game:
        # Reset objects and variables
        game = True
        snake.snake_delete()
        snake = Snake()
        food.new_location()

        # Reset score
        score = 0
        show_score.clear()
        show_score.write(f"Score: {score}", align="center", font=('Arial', 24, 'bold'))
        show_high_score.clear()
        show_high_score.write(f"High Score: {high_score}", align="center", font=('Arial', 24, 'bold'))
        try_again.clear()

        play_game()

# Check food collision
def check_food_collision(snake_head):
    if snake_head.distance(food) <= 10:
        food.new_location()
        snake.add_segment()

        # Change score
        global score, high_score
        score += 1
        high_score = max(high_score, score)
        show_score.clear()
        show_score.write(f"Score: {score}", align="center", font=('Arial', 24, 'bold'))
        show_high_score.clear()
        show_high_score.write(f"High Score: {high_score}", align="center", font=('Arial', 24, 'bold'))

# Check tail collision
def check_tail_collision(snake_head):
    for segment_num in range(1, len(snake.segments)-1):
        if snake_head.distance(snake.segments[segment_num]) <= 10:
            global game
            game = False

# Check wall collision
def check_wall_collision(snake_head):
    if snake_head.xcor() < -300  or snake_head.xcor() > 280 or snake_head.ycor() < -280 or snake_head.ycor() > 300:
        global game
        game = False


play_game()
screen.exitonclick()