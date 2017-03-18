print ("What is your name?")
name = input()
print ("How old are you?")
age = input()
print ("How tall are you?")
height = input()
print ("How much do you weigh?")
weight = input()
print ("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
print ("So, %s, you're %d old, %d tall and %d heavy." % (
    name, age, height, weight))
