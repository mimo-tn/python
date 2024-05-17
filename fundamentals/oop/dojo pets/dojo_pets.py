from my_module.pets import pet
class ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self
class sub_pets(pet):
    def __init__(self,name, type, tricks, noise, age):
        super().__init__(name, type, tricks, noise)
        self.age = age
    def sub_pets_sleep(self):
        super().sleep()
        return self

first_dog = pet("floky","dog"," ","barking")
first_ninja = ninja("med amine","yaakoubi"," ","kibble",first_dog)
first_ninja.walk().bathe()
sub =  sub_pets("floky","dog"," ","barking",5)
sub.sub_pets_sleep()
