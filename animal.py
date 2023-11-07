class Animal:
    def __init__(self, species):
        self.species = species

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}:\nspecies = {self.species!r}\n'


class Human(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}:\nspecies = {self.species!r}\nname = {self.name!r}\n'


class Person(Human):
    def __init__(self, species, name, tax_number):
        super().__init__(species, name)
        self.tax_number = tax_number

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}:\nspecies = {self.species!r}\nname = {self.name!r}\ntax_number = {self.tax_number!r}\n'


class Pet(Animal):
    def __init__(self, species, owner):
        super().__init__(species)
        self.change_owner(owner)
        self.vaccine = None
        self.chip = None

    def change_owner(self, new_owner):
        self.owner = new_owner

    def add_vaccine(self, vaccine):
        self.vaccine = vaccine

    def add_chip(self, chip):
        self.chip = chip

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        additionalString = ''
        if self.chip != None:
            additionalString = f'vaccine = {self.vaccine}\n' 
            
        if self.chip != None:
            additionalString += f'chip = {self.chip}\n' 


        return f'{clsname}:\nspecies = {self.species!r}\nowner = {self.owner.name!r}\n{additionalString}'


animal = Animal("Dog")
human = Human("Human", "John")
person = Person("Human", "Alice", "123-45-6789")
pet = Pet("Cat", owner=person)

print(animal)
print(human)
print(person)
print(pet)  


""""      change owner      """
new_person = Person("Human", "Bob", "987-65-4321")
pet.change_owner(new_person)
print(pet)


""""   add vaccine & chip   """
pet.add_chip('ZCHIPYT')
pet.add_vaccine('HIV')
print(pet)


