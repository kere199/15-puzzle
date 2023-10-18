from turtle import Turtle,Screen
class Board:
    def __init__(self):
     self.t = Turtle()
     self.t.hideturtle()
     self.t.penup()
     self.t.goto(-100,300)
     self.t.setheading(0)
     self.tiles = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,None]]
    #  self.voidpos = self.find_void_position()
          

    def find_void_position(self):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == None:
                    return (i, j)

    def draw_tiles(self):
       for row  in self.tiles:
          for num in row:
             self.t.write(num)
             self.t.forward(50) 
          self.t.goto(-100, self.t.ycor() - 50)


    def swap_with_void(self,pos):
       x1, y1 = pos
       x0, y0 = self.find_void_position()
       self.tiles[x0][y0],self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x0][y0]

    def down(self):
       el_up_pos = (self.find_void_position() [0] -1 , self.find_void_position()[1]) 
       if 0 <= el_up_pos[0] <= 3 and 0 <= el_up_pos[1] <= 3:
        self.swap_with_void(el_up_pos)
        self.t.goto(-100,300)
        self.t.clear()
        self.draw_tiles()

    def up(self):
       el_down_pos = (self.find_void_position()[0] +1  , self.find_void_position()[1]) 
       if 0 <= el_down_pos[0] <= 3 and 0 <= el_down_pos[1] <= 3:
        self.swap_with_void(el_down_pos)
        self.t.goto(-100,300)
        self.t.clear()
        self.draw_tiles()


    def left(self):
       el_right_pos = (self.find_void_position()[0] , self.find_void_position()[1]-1) 
       if 0 <= el_right_pos[0] <= 3 and 0 <= el_right_pos[1] <= 3:
        self.swap_with_void(el_right_pos)
        self.t.goto(-100,300)
        self.t.clear()
        self.draw_tiles()


    def right(self):
       el_left_pos = (self.find_void_position()[0] , self.find_void_position()[1]+1) 
       if 0 <= el_left_pos[0] <= 3 and 0 <= el_left_pos[1] <= 3:
        self.swap_with_void(el_left_pos)
        self.t.goto(-100,300)
        self.t.clear()
        self.draw_tiles()




               
board = Board()
board.draw_tiles()
screen = Screen()
screen.tracer(0)
screen.listen()
screen.onkeypress(fun= board.down, key= "Down" )
screen.onkeypress(fun= board.up, key= "Up" )
screen.onkeypress(fun= board.left, key= "Left" )
screen.onkeypress(fun= board.right, key= "Right" )




screen.exitonclick()