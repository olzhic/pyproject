from random import *
class game:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.rps = ["Rock", "Paper", "Scissors"]
        self.enemy_choice = " "
        self.hero_choice = " "

    def game(self):
        if self.hero.bot:
            self.enemy_choice = choice(self.rps)
            self.hero_choice = choice(self.rps)

            if self.enemy_choice == choice(self.rps):
                print("Draw")
            elif self.enemy_choice == "Rock" and self.hero_choice == "Paper":
                if self.hero.type == "Water":
                    self.hero.waterfall(self.enemy)
                    print(f'Win {self.hero} | {self.enemy}')



