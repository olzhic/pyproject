class Dinosauria:
    def __init__(self, locomotion, tooth_type, pelvic_structure):
        self.locomotion = locomotion
        self.tooth_type = tooth_type
        self.pelvic_structure = pelvic_structure
    def feed(self):
        print("Eating")
class Saurischia(Dinosauria):
    def __init__(self, locomotion, tooth_type, pelvic_structure, feathers):
        super().__init__(locomotion, tooth_type, pelvic_structure)
        self.feathers = feathers

    def feed(self):
        print("Mostly carnivorous and hunting")
class Ornithischia(Dinosauria):
    def __init__(self, locomotion, tooth_type, pelvic_structure, feathers, beak):
        super().__init__(locomotion, tooth_type, pelvic_structure,)
        self.feathers = feathers
        self.beak = beak

Spinosaurus = Saurischia("quadropedal", "Conic", "Lizard_like", "None")
Utahraptor = Saurischia("bipedal", "blade_like", "Lizard_like", "all over the body")
Triceratops = Ornithischia("quadropedal", "Flat", "Bird like", "None", "Present")


