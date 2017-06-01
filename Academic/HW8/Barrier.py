class Barrier(object):
    def __init__(self, n, s, xc, yc, r):
        #defines and sets the attribute and rounds to 1 decimal
        self.name = n
        self.strength = round(float(s),1)
        self.xc = round(float(xc),1)
        self.yc = round(float(yc),1)
        self.radius = round(float(r),1)
    #have a function to output each attribute I need
    def position(self):
        return (self.xc, self.yc)
    def name(self):
        return self.name
    def strength(self):
        strength = self.strength
        if strength <0:
            strength = 0
        return self.strength
    def radius(self):
        return self.radius
    def xpos(self):
        return round(self.xc,1)
    def ypos(self):
        return round(self.yc,1)
    def dxpos(self):
        return round(self.dx,1)
    def dypos(self):
        return round(self.dy,1)    
    
