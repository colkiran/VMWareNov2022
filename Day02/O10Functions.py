

"""
pass arguments to a function there are two ways that we can pass
    1. *args - pass more the one arg and the func will retrieve it and push it appropriate variables

    2. **kwargs = pass named args like a dictionary

"""

def greet():
    print("Greetings Mr. Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# gname is a non default argument, cty is a default argument
def greetGstCty(gname, cty="Mumbai"):
    print(f"Greeting Mr.{gname} from {cty}, Welcome to the event......")

greet()

print("-" * 40)
greetGst("Rahul")
greetGst("Sourav")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
print("-" * 40)

def admsn(name, dob, qlf, gender, adr, conno, city, mrsts):
    print(f"Name           :{name}")
    print(f"DOB            :{dob}")
    print(f"Qualification  :{qlf}")
    print(f"Gender         :{gender}")
    print(f"address        :{adr}")
    print(f"Contact No     :{conno}")
    print(f"City           :{city}")
    print(f"Marital Status :{mrsts}")

# *args
admsn("Kevin", "13/9/1987", 'MBA', 'Male', 'MG Road, 1st Cross', '22567567', 'Bangalore', 'Married')

print("-" * 40)
# **kwargs
admsn(qlf="MBA", adr="Brigade Road, 2nd cross",  name="Tina", conno="2099644", city="Bangalore", dob="9/4/1989", mrsts="Spinster", gender='Female')

print("-" * 40)
# variable length args
def multiplyMe(*numbers):
    print(*numbers)
    print(numbers)
    prod=1
    for number in numbers:
        prod *= number
    return prod

print(f"The result is :{multiplyMe(1, 2, 3, 4, 5)}")

print("-" * 40)

def ExtractMe(**args):
    print("Extract Me")
    for k, v in args.items():
        print(k, "=>", v)

ExtractMe(name="Sachin", age=32, runs=99, oppn='England', venue="lords")

print("-" * 40)

# in python function can return values

def add_ME(x, y):
    return x + y

a = 30
b = 55
print(f"The sum of {a} and {b} is :{add_ME(a, b)}")

print("-" * 40)

def fact(n):
  if n <= 1:
    return 1

  return n* fact(n-1)

print(fact(5))

print("-" * 40)
def fibo(n):
  if n==0 or n==1:
    return n
  return fibo(n-1) + fibo(n-2)

# iter = int(input("Enter the no of iterations :"))
for i in range(8):
    print(fibo(i), end=" ")
print()

print("-" * 40)

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 40)
# doc String

def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)

print("-" * 40)

def fun2(x, y):
    """
    res = fun2(x, y)
    ----------------

    1. res is the sum of two numbers if x and y are integers
    2. res is the concatenation of two strings if x and y are strings
    3. res is an error if the data type of x and y are different

    """
    return(x + y)

print(fun2(10, 20))
print(fun2("hello ", "world"))

print("-" * 40)
help(fun2)