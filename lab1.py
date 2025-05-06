x=5
y=5
r=x+y
# print(type(r))
print(type(str(r)))

print('single quotes')
print("double quotes")
multilineComment = """1
2
3
4
"""
print(multilineComment)

#STRINGS ARE ARRAYS
var1 = "Hello world"
print(var1[0])
print(var1[3])

#LOOPING TROUGH A STRING
for x in var1:
    print(x)

#STRING LENGTH
print(len(var1))

#CHECK STRING
txt = "the best things in life are free! "
print("free" in txt)

#USING IF STATEMENT WITH STRINGS
if "free" in txt:
    print("yes, it is")

#NOT
if "lobster" not in txt:
    print("id doesnt")

##SLICING STRINGS
print(var1[2:5])

#SLICE FROM THE START
print(var1[:5])

#SLICE TO THE END
print(var1[2:])

#NEGATIVE INDEXING
print(var1[-2:-5])

##MODIFY STRINGS
#UPPER CASE
var1 = "Hello, World!"
print(var1.upper())

#LOWER CASE
print(var1.lower())

#REMOVE WHITESPACES
var1 = "Hello, World!   "
print(var1.strip())

#REPLACE STRING
print(var1.replace('Hello',"Hi"))

#SPLIT STRING
print(var1.strip().split(','))

## CONCANATE STRINGS
print("hello lol" + "world mundo")

##FORMAT STRINGS
#formats :.2f - need to learn about it
name = 'Dr. Green thumb'
print(f"my name is {name}")

##ESCAPE CHARACTERS

print("hello gov\'nor")
print("there's anything to do today \\")
print("I gotta feelling \n goood")
print("nememem \r nememem")
print("\t Once upon a time")
print("atacuandonono \b papepipopu")
print("nosequeseso \f kdkdkdkd")
print("octal value \333 ")
print("hex value \2f2f2f ")


