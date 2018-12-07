class Ball():
    def __init__(self, x, y, r, vx = 0, vy = 0, f = 0.05):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.f = f
    

    
    def display(self):
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
        
    def friction(self):
        if self.vx < 0:
            self.vx = self.vx+self.f
        if self.vx > 0:
            self.vx = self.vx-self.f
        if self.vy < 0:
            self.vy = self.vy+self.f
        if self.vy > 0:
            self.vy = self.vy-self.f
        
        if -self.f <self.vx < self.f:
            self.vx = 0
        if -self.f <self.vy < self.f:
            self.vy = 0
        
        
class Table():
    def __init__(self, height = 250, width= 500):
        self.h = height
        self.w = width
        self.balls = []
        
    def createBalls(self):
        self.balls.append(Ball(self.w/2,self.h/2,10,10,10))
        
        
    def display(self):
        rect(0,0,self.w,self.h)
        ellipse(self.balls[0].x, self.balls[0].y, 2*self.balls[0].r, 2*self.balls[0].r)
        

    
    def update(self):
        self.balls[0].x += self.balls[0].vx
        self.balls[0].y += self.balls[0].vy
        self.balls[0].friction()
        if self.balls[0].x + self.balls[0].r >= self.w or self.balls[0].x - self.balls[0].r <= 0:
            self.balls[0].vx = self.balls[0].vx*(-1)
        
        if self.balls[0].y + self.balls[0].r >= self.h or self.balls[0].y - self.balls[0].r <= 0:
            self.balls[0].vy = self.balls[0].vy*(-1)

table = Table()
table.createBalls()

def setup():
    size(table.w,table.h)
    
def draw():
    table.display()
    table.update()
