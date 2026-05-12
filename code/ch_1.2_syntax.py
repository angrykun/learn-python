# 1.2 面向对象


# class
from typing_extensions import Self


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Dog:{self.name},{self.age}"


dog = Dog("tomy", 22)
print(dog)
print(str(dog))


# 集成


class Animal:
    def speak(self):
        return ""


class Cat:
    def __new__(cls, name: str, age: int) -> Self:
        print("from new")
        return super().__new__(cls)

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        print("from init")
        super().__init__()

    def speak(self):
        return "Meow!"


cat = Cat("tom", 11)
print(str(cat))
