from turtle import Turtle




class ScreenDivider():

    def __init__(self, y_positions):

        self.y_positions = y_positions
        self.div = None
        for i in self.y_positions:
            self.create_divider(i)

    def create_divider(self, y_pos):
        self.div = Turtle(shape="divider")
        self.div.color("white")
        self.div.speed("fastest")
        self.div.penup()
        self.div.goto(0, y_pos)







