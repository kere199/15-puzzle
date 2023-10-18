from turtle import Turtle,Screen
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.goto(-100,100)
     self.t.setheading(0)
     self.tiles = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,None]]
     self.voidpos = (3,3)
          

    def draw_tiles(self):
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)


    def swap_with_void(self,pos):
       x1, y1 = pos
       x0, y0 = self.voidpos
       self.tiles[x0][y0],self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x0][y0]

    def down(self):
       el_up_pos = (self.voidpos [0] , self.voidpos[1]) 
       self.swap_with_void(el_up_pos)
               
screen = Screen()

board = Board()
board.draw_tiles()