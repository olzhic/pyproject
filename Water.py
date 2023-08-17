class Water_Wizard:
    def __init__(self, hp, dmg, mana):
        self.hp = hp
        self.dmg = dmg
        self.type = "Water"
        self.mana = mana
    def waterfall(self, entity):
        if entity.type == "fire":
            entity.setHp(self.dmg)
            self.setMana(self.dmg)
        else:
            entity.setHp(-1 * self.dmg)
            self.setMana(self.dmg)

    def setHp(self, hp):
        self.hp -= hp

    def setMana(self, mana):
        self.mana -= mana

    def __str__(self):
        return f'{self.hp}|{self.type}|{self.mana}'

