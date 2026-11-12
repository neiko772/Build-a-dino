class Dino: 
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species 
        self.diet = diet
        self.age = age

    def roar(dino):
        return f"{dino.name} the {dino.species} roars loudly!"

    def eat(dino, food):
        if food.lower() in dino.diet:
            return f"{dino.name} is eating {food}."
        else:
            return f"{dino.name} does not eat {food}."

    def dino_info(dino):
        return f"{dino.name} is a {dino.age}-year-old {dino.species} that eats {',' .join(dino.diet)}."