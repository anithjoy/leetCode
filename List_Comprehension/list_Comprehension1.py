#  here we are going to learn about list comprehension

# ability to construct list from another existing list 

# for loop

fruits = ["apple", "orange", "strawberry" ]

[print(fruit) for fruit in fruits ]
capitalFruits = [fruit.upper() for fruit in fruits]
capitalFruits.append("Watermelon")
print(capitalFruits)

# --------------------------------------------------------------------------------------#
# example 2

bits = [True, False,True, False, False, True, False, True,True, True, False]

# return 1 if true else 0 if false
newBits = [1 if bit is True else 0 for bit in bits]
print("New Bits -> ",newBits)

# --------------------------------------------------------------------------------------#
#  String manipulation
mySTring = "HelloMyNameIsMariya"

spaceString = "".join([i if i.islower() else " "+i.lower() if i in ["I","N"] else " "+i for i in mySTring] ).strip()
# return result ---- if (condition) ---- else return result if (condition) ---- else return result
# similar to if , elif, else

print("[String with spaces]",spaceString)