#practice
class Weapon:
    def __init__(self, damage, firerate, ammocapacity):
        self.damage = damage
        self.firerate = firerate
        self.ammocapacity = ammocapacity

    def setDamage(self, damage):
        self.damage = damage
    def setFirerate(self, firerate):
        self.firerate = firerate
    def setAmmocapacity(self, ammocapacity):
        self.ammocapacity = ammocapacity

pistol = Weapon(20, 250, 12)
print(pistol.damage)
rifle = Weapon(70, 500, 30)
print(rifle.firerate)

pistol.setDamage(30)
print(pistol.damage)
