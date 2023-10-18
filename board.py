from turtle import Turtle,Screen
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.goto(-100,100)
     self.t.setheading(0)
     self.tiles = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,None]]
     self.y = 100


          

    def draw_tiles(self):
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)
        
screen = Screen()     


board = Board()
board.draw_tiles()