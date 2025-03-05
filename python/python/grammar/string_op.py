#!python3
# -*- coding: utf-8 -*-
# string_op.py - string operation

name = "Alice"
age = 20


# combine
print("Hello, " + name + "!")
print("You are " + str(age) + " years old.")

print(f"Hello, {name}, you are {age}!")

print("Hello, %s, you are %d!" % (name, age))
print("Hello, {name}, you are {age}!".format(name=name, age=age))
print("Hello, {0}, you are {1}!".format(name, age))
print("Hello, {}, you are {}!".format(name, age))

# repeat
print("Hello, " * 3)  # Hello, Hello, Hello,


# upper and lower
print(name.upper())  # ALICE
print(name.lower())  # alice
print(name.capitalize())  # Alice
print(name.title())  # Alice

print("hello-world".title())  # Hello World
print("hello world".capitalize())  # Hello world


## string split and join
s = "hello, world"
print(s.split())  # ['hello,', 'world']
print(s.split(","))  # ['hello', ' world']

print(" ".join(["Hello", "World"]))  # Hello World
