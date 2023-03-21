class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof! Woof!")


class DogOwner:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def walk_dog(self):
        print(f"{self.name} is walking {self.dog.name}")


dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Charlie", "Beagle", 2)
owner1 = DogOwner("Alice", dog1)
owner2 = DogOwner("Bob", dog2)

dog1.bark()
owner2.walk_dog()
dog2.bark()
owner1.walk_dog()
