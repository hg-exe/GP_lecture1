print("Harry")
print(29)

pet_name = "Penny"
pet_age = 8

print(pet_name + str(pet_age))

number_1 = 10
number_2 = 16

# ACTIVITY 2
total_price = 0
amongus = 12
eldenring = 60
projectgrove = 20
us_tax = 1.14

total_price += (amongus + eldenring + projectgrove)
total_price *= us_tax

print("Your total price is: $" + str(total_price))

#exercise 4
name = "My name"
print("Your name is %s" % (name))
###
age = 12
height = 1.68

print("Your name is %s, your age is %d and you are %f cm tall" % (name, age, height))

name =  "Harry"
age = 12
height = 1.6867

print("Your name is {}, your age is {:.2f} and you are {:.2f} tall".format(name, age, height))

#exercise 5


#exercise 6

number = int(input("Give me a number: "))

if number < 100:
    print("That’s a small number")
elif number <= 1000:
    print ("That’s not a big number yet")
else:
    print("That's a big number")


if number % 2 == 0:
    print("Even")
else:
    print("Odd")