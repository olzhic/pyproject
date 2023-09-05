class Fire_Wizard:
    def __init__(self, hp, dmg, mana, isbot):
        self.hp = hp
        self.dmg = dmg
        self.type = "Fire"
        self.mana = mana
        self.isbot = isbot

    def fireball(self, entity):
        if entity.type == "Water":
            entity.setHp(self.dmg)
            self.setMana(self.dmg)
        elif entity.type == "Fire":
            entity.setHp(-1 * self.dmg)
            self.setMana(self.dmg)


    def setHp(self, hp):
        self.hp -= hp

    def setMana(self, mana):
        self.mana = mana

    def __str__(self):
        return f"{self.hp}|{self.type}|{self.mana}"
