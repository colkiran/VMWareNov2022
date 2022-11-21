
# emulate C style - printf
format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")           # tuple
print(f"values :{values}")
print(format % values)

print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.882929, "class"))

print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.88769, "class"))

print("-" * 40)
# emulate unix shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(f"tmpl :{tmpl}")
res = tmpl.substitute(name="Sachin", adj="superb")
print(res)

print("-" * 40)
# format strings from python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("India", "Sachin", "class"))
print("Welcome {name}, what a {adj} player for {ctry}".format(ctry = "India", name = "Sachin", adj = "class"))
print("Welcome {name}, your rating of {rating}, what a {adj} player".format( name = "Sachin", rating = 4.879092,adj = "class"))
print("Welcome {name}, your rating of {rating:.3f}, what a {adj} player".format( name = "Sachin", rating = 4.879092,adj = "class"))

# interpolation
from math import pi, e
print(f"PI = {pi} and Euler's constant = {e}")

print("PI = {} and Euler's constant = {}".format(pi, e))
print("PI = {0} and Euler's constant = {1} and magic number = {2}".format(pi, e, 40585))
print("PI = {0} and Euler's constant = {1} and magic number = {magic}".format(pi, e, magic = 40585))

print("-" * 40)
full_name = ['Sachin', 'Tendulkar']
print("Mr.{name}".format(name= full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))

print("-" * 40)
print(__name__)                 # name of the module - __main__
import math
print(math.__name__)

print("The {mod.__name__} module gives the value of pi = {mod.pi} and euler's constant e = {mod.e}".format(mod=math))

# import sys
# print(sys.argv[0])              # Filename

print("conversions".center(40, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 40)
print("The number {num} {num} {num}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3678596712))
print("The number {num:10} {num:f} {num:b}".format(num=36))

print("-" * 40)
print("{num:15} Tendulkar".format(num = 33))
print("{num:15} Tendulkar".format(num = "Sachin"))

print("-" * 40)
print("{}".format("Sachin Tendulakar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
print("{num:>15} Tendulkar".format(num="Sachin"))            # right aligned
print("{num:^15} Tendulkar".format(num="Sachin"))            # Center aligned
print("{num:<15} Tendulkar".format(num="Sachin"))            # left aligned

print("-" * 40)
print("{num:*^40}".format(num="Sachin"))
print("{:*^40}".format("Sachin"))
print("Sachin".center(40, "*"))

print("-" * 40)
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))
