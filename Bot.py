from random import *
class bot:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.rps = ["Rock", "Paper", "Scissors"]
        self.enemy_choice = " "
        self.hero_choice = " "

    def game(self):
        if self.hero.isbot == True:
            while True:

                self.enemy_choice = choice(self.rps)
                self.hero_choice = choice(self.rps)

                if self.enemy_choice == choice(self.rps):
                    print(self.enemy_choice)
                    print("Draw")
                elif self.enemy_choice == "Rock" and self.hero_choice == "Paper":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Rock" and self.hero_choice == "Scissors":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Paper" and self.hero_choice == "Scissors":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Paper" and self.hero_choice == "Rock":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Scissors" and self.hero_choice == "Rock":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Scissors" and self.hero_choice == "Paper":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')

                    if self.enemy.hp <= 0:
                        print("Your ally won")
                        break

                    if self.hero.hp <= 0:
                        print("Your ally died")
                        break

    def game_not_bot(self):
        if self.hero.isbot == False:
         while True:
                self.enemy_choice = choice(self.rps)
                self.hero_choice = input(self.rps)

                if self.enemy_choice == self.hero_choice:
                    print(self.enemy_choice)
                    print("Draw")
                elif self.enemy_choice == "Rock" and self.hero_choice == "Paper":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Rock" and self.hero_choice == "Scissors":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Paper" and self.hero_choice == "Scissors":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Paper" and self.hero_choice == "Rock":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Scissors" and self.hero_choice == "Rock":
                    if self.hero.type == "Water":
                        self.hero.waterfall(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} | {self.enemy}')
                    elif self.hero.type == "Fire":
                        self.hero.fireball(self.enemy)
                        print(self.enemy_choice)
                        print(f'Win {self.hero} / {self.enemy}')
                elif self.enemy_choice == "Scissors" and self.hero_choice == "Paper":
                    if self.enemy.type == "Water":
                        self.enemy.waterfall(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} | {self.enemy}')
                    elif self.enemy.type == "Fire":
                        self.enemy.fireball(self.hero)
                        print(self.enemy_choice)
                        print(f'Loss {self.hero} / {self.enemy}')
                if self.enemy.hp <= 0:
                    print("You win")
                    break

                if self.hero.hp <= 0:
                    print("You died")
                    break



