class Ball(object):
    def __init__(self,x,y,dx,dy,r,c):
        self.ball_x = int(x)
        self.ball_y = int(y)
        self.ball_dx = int(dx)
        self.ball_dy = int(dy)
        self.ball_radius = int(r)
        self.ball_color = c
    def position(self):
        output = (self.ball_x, self.ball_y)
        return output
    def check_and_reverse(self, maxx, maxy):
            if self.ball_x - self.ball_radius <= 0 or self.ball_x + self.ball_radius >= maxx:
                self.ball_dx *= -1
            if self.ball_y - self.ball_radius <= 0 or self.ball_y + self.ball_radius >= maxy:
                self.ball_dy *= -1  
                
        
    def move(self):
        #Ball.check_and_reverse(self,maxx,maxy)
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy
        
        
    def bounding_box(self):
        bound_box = (self.ball_x-self.ball_radius, self.ball_y-self.ball_radius, self.ball_x+self.ball_radius, self.ball_y+self.ball_radius)
        return bound_box
    def get_color(self):
        return self.ball_color
    def some_inside(self, maxx, maxy):
        self.maxx = maxx
        self.maxy = maxy
        self.isstopped = False
        if 0 < self.ball_x + self.ball_radius and self.ball_x - self.ball_radius < self.maxx and 0 < self.ball_y + self.ball_radius and self.ball_y - self.ball_radius < self.maxy and not self.isstopped:
            return True
        else:
            return False
    
        
