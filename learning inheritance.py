# define a new class called animal
# Animal will be the "super" class - the class other classes will inherit from

class Animal():
    def __init__(self):
        self.num_eyes = 2
        self.num_noses = 1
        # so these are the attributes of the animal

    def breathe(self):
        print("Inhale and Exhale")
        # animal class methods


# now I will create a new class called fish that will inherit attributes and methods from animal

class Fish(Animal):
    def __init__(self):
        super().__init__()

    # now the fish class has the exact same attributes and methods as the animal class
    # so i can print fish.num_eyes and will still print 2 or same with method
    # fishy = Fish()
    # fishy.breathe() = inhale and exhale

    # to modify a method in a new class do this below
    def breathe(self):
        super().breathe()
        print("A fish breathes underwater ")

    # this will print same as above so inhale and exhale but will now also print a fish breathes underwater
    # you can also add new methods separate to super class
    def swim(self):
        print("Moving forward in the water ")
