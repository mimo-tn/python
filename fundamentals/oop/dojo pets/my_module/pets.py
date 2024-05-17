class pet:
    energy = 100
    health = 100
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.nois =  noise
    def sleep(self):
        self.energy += 25 
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.nois)
        return self
