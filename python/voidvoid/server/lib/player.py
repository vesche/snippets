
class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.max_hp = 100
        self.hp = self.max_hp
        self.inventory = []
    
    def hurt(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.alive = False
            self.hp = 0
    
    def heal(self, amount):
        if self.hp == 0:
            return

        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def del_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
    
    def revive(self):
        self.alive = True
        self.hp += 1