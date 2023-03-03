import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'  
        self.startNew()
        self.addBlock((0,10, 0))
    def delBlock(self, position):
       """удаляет блоки в указанной позиции """
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        self.block.setTag("at", str(position))
    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y

    def saveMap(self):
       blocks = self.land.getChildren()
       with open('my_map.dat', 'wb') as fout:
           pickle.dump(len(blocks), fout)
           for block in blocks:
               x, y, z = block.getPos()
               pos = (int(x), int(y), int(z))
               pickle.dump(pos, fout)
            
    def loadMap(self):
       self.clear()
       with open('my_map.dat', 'rb') as fin:
           length = pickle.load(fin)
           for i in range(length):
               pos = pickle.load(fin)
               self.addBlock(pos)