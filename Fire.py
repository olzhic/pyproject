class Fire_Wizard:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg
        self.type = "fire"

    def fireball(self, entity):
        if entity.type == "Water":
            entity.setHp(self.dmg)
        else:
            entity.setHp(-1 * self.dmg)


    def setHp(self, hp):
        self.hp -= hp

    def __str__(self):
        return f"{self.hp}|{self.type}"
