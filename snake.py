from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.start_snake()

    def snake_delete(self):
        for segment in self.segments:
            segment.reset()

    def start_snake(self):
        for i in range(0, 3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=i * -20, y=0)
            self.segments.append(new_segment)
        self.segments[0].color("green")

    def get_head(self):
        return self.segments[0]

    def add_segment(self):
        new_x = self.segments[0].xcor()
        new_y = self.segments[0].ycor()
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=new_x, y=new_y)
        self.segments.append(new_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
