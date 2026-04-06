# Object Types / Data Types

- Numbers:  int (e.g. 42) — immutable
  float (e.g. 3.14) — immutable
  complex (e.g. 1+2j) — immutable

- Boolean:
  bool (True / False) — immutable

- Text / Bytes:
  str (e.g. "hello") — immutable
  bytes (e.g. b'abc') — immutable
  bytearray (e.g. bytearray(b'abc')) — mutable

- Sequences:
  list (e.g. [1, 2, 3]) — mutable
  tuple (e.g. (1, 2, 3)) — immutable
  range (e.g. range(5)) — immutable (sequence-like)

- Sets / Frozen sets:
  set (e.g. {1, 2, 3}) — mutable
  frozenset (e.g. frozenset({1,2})) — immutable

- Mappings:
  dict (e.g. {'a': 1}) — mutable

- Special / Others:
  NoneType (None) — immutable (singleton)
  memoryview — mutability depends on underlying buffer
  functions, classes, modules — objects (their attributes may be mutable)

- Notes:
"Mutable" means the object's contents can be changed in place (e.g., list.append, dict[key]=value).
"Immutable" means operations produce new objects; the original cannot be changed (e.g., string.replace returns a new str).
A container can be immutable while containing mutable items (e.g., a tuple can contain a list; the tuple cannot be re-assigned but the inner list can be mutated).

- Quick examples:
Mutable (list)
   lst = [1, 2]; lst[0] = 10  # modifies same object
Immutable (tuple / str)
  t = (1, 2);  # cannot assign t[0] = 10
  s = "hi"; s2 = s.upper()  # s unchanged, s2 is new object


# Numbers in python:

Basic is same as other languages and following are the changes:
x=2,y=3,z=4
print x,y,z
>>(2,3,4)

**multipy will raise the number to the power like
2*3=6
2**3=8
//double divide will give floor divide

-10/3=-3.33
-10//3=-4


- repr(obj)
  - Intended for developers/debugging.
  - Should produce an “official” string representation that, when possible, can be used to recreate the object.
  - Used by the interactive REPL and by repr().
  - Example: repr("hi") -> "'hi'"

   repr shows quotes for strings and more details; str is nicer for humans.
  - If a class defines both __repr__ and __str__, print(obj) uses __str__; repr(obj) uses __repr__. If __str__ is missing, Python falls back to __repr__.

  # Octal,Binary,Hexadecimal

  - Octal literals start with `0o` or `0O` (e.g., `0o17` is 15 in decimal).
  - Binary literals start with `0b` or `0B` (e.g., `0b101` is 5 in decimal).
  - Hexadecimal literals start with `0x` or `0X` (e.g., `0xFF` is 255 in decimal).
  - These are alternative ways to represent integers in Python. You can convert between them using functions like `oct()`, `bin()`, and `hex()`.

  Example:
  python
  print(0o17)  # Output: 15
  print(0b101) # Output: 5
  print(0xFF)  # Output: 255

  # Converting integers to other bases:
  x = 255
  print(oct(x))  # Output: '0o377'
  print(bin(x))  # Output: '0b11111111'
  print(hex(x))  # Output: '0xff'
  
  The conversion can also take place by 
  using format() or f-strings:
  x = 255
  print(f'{x:o}')  # Octal: 377
  print(f'{x:b}')  # Binary: 11111111
  print(f'{x:x}')  # Hexadecimal: ff (lowercase)
   
  And
  int ('101', 2)  # Output: 5
  int ('ff', 16)  # Output: 255
  and so on

  # import random
  import random

  - Generate a random float between 0.0 and 1.0
print(random.random())

- Generate a random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))
  - Output: 0.423456789 (example)
  - Output: 7 (example)
  
  choice, shuffle etc

  import decimal from Decimal,
  import fraction from Fraction
  etc

# Sets
setone ={1,2,3,4}
setone & {1,3} #intersection
set() #empty set

# String
'' ,"",""" """
and 
slice in string with hop[0:7:2]
lower(),upper(),replace()
chai.lower/chai.upper/chai.replace
chai.split("by default space but user can specify based on what the split is needed")
x="Utkarsh"
y=3
z="Hello {} You have logged in for {} times"
print(z.format(x, y))
- output: Hello Uttkarsh you have logged in for 3 times
len(z)

# List/Array
x=[]
print(" ".join(variable name))
x.append("")
x.pop()
x.remov("")
x.insert(1,"")
x=[y**3 for y in range(5)]

# Dictionaries
x={"name":"Utkarsh","age":20}
x["name"]="Utkarsh"
x.get("name")
x.keys()
x.values()
x.items()

del deletes from refrence
del x ["name"]
x.pop("name")  
# Tuples
x=(1,2,3)
x[0]=1 #immutable

# Typecasting
int(),float(),str(),list(),tuple(),set(),dict()
x=5
print(type(x)) #output: <class 'int'>
