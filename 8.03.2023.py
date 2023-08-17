class Weapon:
    def __init__(self, ammomag, ammogen):
        self.ammomag = ammomag
        self.ammogen = ammogen
        self.ammosize = ammomag


    def shoot(self):

        if self.ammomag == 0:
           if self.ammogen == 0:
               return 1
           self.reload()
        print(self.ammomag)
        self.ammomag -= 1
        self.shoot()


    def reload(self,):
        self.ammomag = self.ammosize
        self.ammogen -= self.ammosize



        print(self.ammogen)
        self.shoot()

    def shootmenu(self):
        print("You've got a pistol, dou you want to try is out?")
        a = input("Yes or No? ")
        if a == "Yes":
            print("Shooting...")
            self.shoot()
            print("ammo out")

        elif a == "No":
            print("Ok, nevermind")

pistol = Weapon(12, 36)
pistol.shootmenu()




