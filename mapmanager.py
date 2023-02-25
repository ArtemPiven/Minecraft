import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = '11.jpg'
        self.texture2 = 'Stone_29_JE5_BE3.webp'
        self.color = (0.2, 0.2, 0.35, 1) #rgba
        self.addBlock((0,10,0))
        self.addBlock((1,10,0))
        # новый узел карты
        self.startNew()
        #создаем блок

    def StartNew(self):
        #створюємо основу для нової карти
        self.land = render.attachNewNode("Land") #вузол до якого прив'язані всі блоки
        
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.setTag("at", str(position))
        self.block.reparentTo(self.land)
    def find_Blocks(self, pos):
        return self.land.findAllMatches("=at=", str(pos))
    def delBlock(self, pos):
        blocks = self.find_Blocks(pos)
        for block in blocks:
            block.removeNode()
    def saveMap(self):
        blocks = self.land.getChildren()
        with open("my_map.dat", "wb") as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)
    def loadMap(self):
        self.Clear()
        with open("my_map.dat", "wb") as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)
    def Clear(self):
        #очистка карти
        self.land.removeNode()
        self.StartNew()
    def loadLand(self, filename):
        self.Clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    z = 0
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y
    

    

    
                