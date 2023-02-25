

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.setModel(" ")
        self.hero.setTexture(loader.loadTexture(" "))
        self.hero.setScale(1)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
    def camera_bind(self):
        base.camera.setH(180) 
        base.camera.reparentTo(self.hero) 
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True 
        base.disableMouse() 

    def cameraUp(self):
        pos = self.hero.getPos() 
        base.camera.reparentTo(render) 
        base.enable.Mouse()
        self.cameraOn = False
        base.mouseInterfaceNode.setPos(pos[0], pos[1], pos[2]+3)
    def changeView(self): 
        if self.cameraOn:
            self.cameraUp()
        else:
            self.camera_bind()
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        x_from=round(self.hero.getX())
        y_from=round(self.hero.getY())
        z_from=round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from*dx
        y_to = y_from*dy
        return x_to, y_to, z_from
    def check_dir(self, angle):
        if angle >= 0 and angle <= 28:
            return(0, -1)
        elif angle <= 65:
            return(1, -1)
        elif angle <= 110:
            return(1, 0)
        elif angle <= 155:
            return(1, 1)
        elif angle <= 200:
            return(0, 1)
        elif angle <= 245:
            return(-1, 1)
        elif angle <= 290:
            return(-1, 0)
        elif angle <= 335:
            return(-1, -1)
        else:
            return(0, -1)
    def Grow(self):
        self.land.block.setTexture(loader.loadTexture(self.texture1))
        angle = (self.hero.getH())%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        self.land.add_Block(pos)
    def Grow(self):
        self.land.block.setTexture(loader.loadTexture(self.texture2))
        angle = (self.hero.getH())%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        self.land.add_Block(pos)
    def forward(self):
        angle = (self.hero.getH())%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def back(self):
        angle = (self.hero.getH()+180)%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def left(self):
        angle = (self.hero.getH()+90)%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def right(self):
        angle = (self.hero.getH()+270)%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def up(self):
        z = self.hero.getZ()
        self.hero.setZ(z+1)
    def down(self):
        z = self.hero.getZ()
        self.hero.setZ(z-1)
    def build(self):
        angle = (self.hero.getH())%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        self.land.add_Block(pos)
    def destroy(self):
        angle = (self.hero.getH())%360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        self.land.del_Block(pos)
    def accept_events(self):
        base.accept("c", self.changeView)
        base.accept("q", self.turn_left)
        base.accept("q" + "-repeat",self.turn_right)
        base.accept("e", self.turn_left)
        base.accept("e" + "-repeat",self.forward)
        base.accept("w", self.forward)
        base.accept("w" + "-repeat",self.forward)
        base.accept("s", self.back)
        base.accept("s" + "-repeat",self.back)
        base.accept("a", self.left)
        base.accept("a" + "-repeat",self.left)
        base.accept("d", self.right)
        base.accept("d" + "-repeat",self.right)
        base.accept("z", self.up)
        base.accept("z" + "-repeat",self.up)
        base.accept("x", self.down)
        base.accept("x" + "-repeat",self.down)
        base.accept("mouse1", self.build)
        base.accept("mouse3", self.destroy)
        base.accept("k", self.land.saveMap)
        base.accept("l", self.land.loadMap)
        base.accept("1", self.land.Grow)
        base.accept("2", self.land.Stone)

