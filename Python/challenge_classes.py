

class Dog:

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    doginfo = "Human's best friend"

    def bark(self):
        print("BARK!")

    def info(self):
        return self.name, self.age, self.furcolor


mydog = Dog("fido", 12, "brown")

print(mydog.info())
