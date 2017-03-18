my_name = 'Jens Klæbel'
my_age = 58 # not a lie
my_height = 1.90 # inches
my_weight = 100 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Grey'

print ("Let's talk about %s." % my_name)
print ("He's %d cm tall." % (my_height*100))
print ("He's %d kg heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("His BMI is %d." %(my_weight/my_height/my_height))
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))
