class Bird(object):
    def __init__( self, n, m, x0, y0, r0, dx0, dy0):
        #defines and sets the attribute and rounds to 1 decimal
        self.name = n
        self.mass = round(float(m),1)
        self.x = round(float(x0),1)
        self.y = round(float(y0),1)
        self.radius = round(float(r0),1)
        self.dx = round(float(dx0),1)
        self.dy = round(float(dy0),1)
    #have a function to output each attribute I need
    def position(self):
        return (self.x, self.y)
    def radius(self):
        return self.radius
    def name(self):
        return self.name
    def fly(self):
        #adds the veolocity to the bird so it flys
        self.x += self.dx
        self.y += self.dy
    def speed(self):
        return(self.dx, self.dy)
    def lowerspeedpig(self):
        #when a bird hits a pig its x velocity is divided by 2
        self.dx/=2
    def damagegiven(self):
        #calculates velocity using dx dy
        vel = round(((self.dx**2 +self.dy**2)**.5),1)
        #damage = m*v^2 needed for damage to barrier
        damage = round((self.mass * (vel**2)),1)
        return damage
    def birdvelocity(self):
        vel = round(((self.dx**2 +self.dy**2)**.5),1)
        return vel
    def xpos(self):
        return round(self.x,1)
    def ypos(self):
        return round(self.y,1)
    def dxpos(self):
        return round(self.dx,1)
    def dypos(self):
        return round(self.dy,1)    
    def inboard(self):
        #make sure bird is in boarder
        if (self.x - self.radius) <0 or (self.x + self.radius) > 1000:
            return True #if true bird leaves boarder
        if (self.y - self.radius) <0 or (self.y + self.radius) > 1000:
            return True 
        else:
            return False #opposite for True
        
        