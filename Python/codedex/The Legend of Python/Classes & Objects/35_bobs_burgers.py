class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

takeout = Restaurant()
takeout.name = 'Takeout'
takeout.category = 'Fast-food joint'
takeout.rating = 4
takeout.delivery = True

mad_chef = Restaurant()
mad_chef.name = 'Mad Chef'
mad_chef.category = 'Bangladeshi Restaurant'
mad_chef.rating = 3.5
mad_chef.delivery = False

print(vars(bobs_burgers))
print(vars(takeout))
print(vars(mad_chef))