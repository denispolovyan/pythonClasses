class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Pet(Animal):
    def __init__(self, name, species, owner):
        super().__init__(name, species)
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __repr__(self):
        return f'{self.__class__.__name__}: \npet name = {self.name!r} \npet species = {self.species!r} \npet owner = {self.owner!r}\n'

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f'Owner \nowner name = {self.name!r} \nowner age = {self.age!r} \nowner sex = {self.sex!r}\n'

class Owner_and_pet(Person):
    def __init__(self, name, age, sex, pet):
        super().__init__(name, age, sex)
        self.pet = pet

    def change_pet(self, new_pet):
        self.pet = new_pet

    def __repr__(self):
        return f'Owner and pet: \npet name = {self.pet.name!r} \npet species = {self.pet.species!r} \nowner name = {self.name!r} \nowner age = {self.age!r}\nowner sex = {self.sex!r}\n'


owner = {'owner': 'Alex', 'age': 30, 'sex': 'male'}

pet = Pet("Rex", "Lizard", owner['owner'])
person = Person(owner['owner'], owner['age'], owner['sex'])
owners = Owner_and_pet(owner['owner'], owner['age'], owner['sex'], pet)
     
print(pet) 
print(person)     
print(owners)

new_pet = Pet("Sharik", "Cat", "John")
owners.change_pet(new_pet)
print("Owner with new pet:")
print(owners)

pet.change_owner("Alice")
print("Pet with new owner:")
print(pet)

