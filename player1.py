class Player:
    def __init__(self, window, color, xPos, yPos, length, width, speed):
        self.window_ = window
        self.color_ = color
        self.xPos_ = xPos
        self.yPos_ = yPos
        self.length_ = length
        self.width_ = width
        self.speed_ = speed

    def getPos(self):
        print("x: ", self.xPos_, " y: ", self.yPos_)
