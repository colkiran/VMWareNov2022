"""
1. integer
2. float
3. complex numbers
"""

a = 10
b = -10

# f - fstring or format string - interpolation
print(f"a :{a}")
print(type(a))              # RTTI = runtime type identifier
print(f"b :{b}")
print(type(b))

print("-" * 40)

c = 10.0
d = -10.0

print(f"c :{c}")
print(type(c))

print(f"d :{d}")
print(type(d))

print("-" * 40)

e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g = 3 + 4j
h = 3 - 4j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
print(max(10, 25, 15))
print(min(10, 25, 15))

x =  3 + 2.5
print(f"x :{x}")
print(type(x))

print("-" * 40)

x = 1
y = 2.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("coversion".center(40, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)       # decimal number
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o101)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(40,"-"))
a = 100
print(oct(a))
print(hex(a))
print(bin(a))

"""
identifiers
    a. case sensitive
    b. must not be python keywords
"""

