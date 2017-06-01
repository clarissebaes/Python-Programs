class Pig(object):
    def __init__( self, n, xc, yc, r0 ):
        #defines and sets the attribute and rounds to 1 decimal
        self.name = n
        self.x = round(float(xc),1)
        self.y = round(float(yc),1)
        self.radius = round(float(r0),1)
    #have a function to output each attribute I need
    def position(self):
        return (self.x, self.y)
    def name(self):
        return self.name
    def radius(self):
        return self.radius
    def xpos(self):
        return round(self.x,1)
    def ypos(self):
        return round(self.y,1)    