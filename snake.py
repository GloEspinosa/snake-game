from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_MOVED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # TODO 1. Create a snake body  (3 squares)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        # square.speed("slow")
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        """This function adds a new segment to use it each time the snake gets food."""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            # Making snake disappear when new one appears
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # TODO 3. Control snake

    def move(self):
        """Cada cuadrado pasa a la posición del anterior, y el primero se mueve hacia delante. """
        # for square in range(start=2, stop=0, step=-1):
        # for square in range(2, 0, -1):
        for square in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square - 1].xcor()
            new_y = self.segments[square - 1].ycor()
            self.segments[square].goto(new_x, new_y)
        self.head.forward(DISTANCE_MOVED)
        # self.segments[0].right(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

