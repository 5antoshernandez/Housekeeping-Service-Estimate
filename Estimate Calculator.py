

#price_per_bedroom = 10

#small_bathroom = 20
#medium_bathroom = 25
#large_bathroom = 30

#small_kitchen = 20
#medium_kitchen = 25
#large_kitchen = 30

#small_fridge = 30
#medium_fridge = 35
#large_fridge = 45

#oven = 45

#small_inside_window = 7.5
#medium_inside_window = 10
#large_inside_window = 12.5

### per 100 sq ft charge $10 extra

#heavy_duty = 50

#fan = 5

#deep cleaning = 2 * regular_price
#movein_moveout =
brnumber = input("How many bedrooms?")
bathnumber = input("How many bathrooms?")
sqftnumber = input("Sqft of your house?")
pets = input("Do you have pets? Y for Yes, N for no.")
frequency = input("How frequent will you be needing services?")
regService = input("Would you like regular servicing? Y for Yes, N for No.")
kitchen = input("Will you be needing your kitchen cleaned? Y for Yes, N for No.")
extraServices = input("Are you interested in extra services?")
interior_windows = input("Would you like your interior windows cleaned?")
blinds = input("Would you like your blinds cleaned?")
fridge = input("Would you like your fridge cleaned?")
oven = input("Would you like your oven cleaned?")

class Estimate:
    def __init__(self, brnumber, bathnumber, kitchen, regService, sqftnumber, pets, frequency):
        self.brnumber = int(brnumber)
        self.bathnumber = int(bathnumber)
        self.kitchen = str(kitchen)
        self.regService = str(regService)
        self.sqftnumber = int(sqftnumber)
        self.pets = str(pets)
        self.frequency = frequency
class xtraServices:
    def __init__(self, interior_windows, fridge, oven, blinds):
        self.interior_windows = interior_windows
        self.fridge = fridge
        self.oven = oven
        self.blinds = blinds

def estimate(object):
    total_cost = 0
    if object.frequency == "weekly":
        total_cost = -5
    if object.frequency == "biweekly":
        print("By choosing biweekly, you saved $20 on your monthly bill!")
    if object.frequency == "monthly":
        total_cost += 10
        print("By choosing monthly, you saved $10 on your monthly bill!")
    if object.regService == "N" or "n":
        total_cost += 20
    ### adding cost of bedrooms
    total_cost += (10 * object.brnumber)
    ### adding cost of bathrooms
    total_cost += (20 * object.bathnumber)
    ### adding cost of sqft
    if object.sqftnumber > 500:
        total_cost = (object.sqftnumber - 500) * .07
    ### adding cost of kitchen
    if object.kitchen == "Y" or "y":
        total_cost += 2
   ### adding cost of pets
    if object.pets == "Y" or "y":
        total_cost += 25
    if object.extraServices == "Y" or "y":
        extraServicesfunct(object)
    return ("Your estimate will be between:", total_cost - 10, "-", total_cost + 10)
def extraServicesfunct(object)
    total_cost = 0
    if object.interior_windows == "Y" or "y":
        total_cost += 7.5
    if object.fridge == "Y" or "y":
        total_cost += 35
    if object.oven == "Y" or "y":
        total_cost += 45
    if object.blinds == "Y" or "y"
        total_cost += 30
    return total_cost
#Person1Estimate = Estimate(brnumber, bathnumber, kitchen, regService, sqftnumber, pets, frequency)
Person1ExtraServices = xtraServices(interior_windows, fridge, oven, blinds)
#print(estimate(Person1Estimate))
#print(extraServicesfunct(Person1ExtraServices))
#runAnother = input("Would you like to run another estimate?")
#print(runAnother)
#if runAnother == "Y" or "y":
    #print(estimate(Person2))