#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print("Hello, " + name + "!")
greet("Alice")


def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")
greet_with_default("Alice")

def add(num1, num2):
    return num1 + num2
add(45,55)

def halve(number):
    return number / 2
halve(45)
    
