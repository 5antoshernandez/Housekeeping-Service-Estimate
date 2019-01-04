

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
full_cost = 0
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
    def __init__(self, brnumber, bathnumber, kitchen, regService, sqftnumber, pets, frequency, full_cost = 0):
        self.brnumber = int(brnumber)
        self.bathnumber = float(bathnumber)
        self.kitchen = str(kitchen)
        self.regService = str(regService)
        self.sqftnumber = int(sqftnumber)
        self.pets = str(pets)
        self.frequency = frequency
        self.full_cost = 0
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
    object.full_cost += total_cost
    return "Your estimate will be between: " + "$" + str(object.full_cost - 10) + " - " + "$" + str(object.full_cost + 10)
def extraServicesfunct(object):
    total_cost_ext = 0
    if object.interior_windows == "Y" or "y":
        how_many_windows = input("How many windows do you have?")
        print(how_many_windows)
        total_cost_ext += 7.5 * int(how_many_windows)
    if object.fridge == "Y" or "y":
        total_cost_ext += 35
    if object.oven == "Y" or "y":
        total_cost_ext += 45
    if object.blinds == "Y" or "y":
        total_cost_ext += 30
    Person1Estimate.full_cost += object.total_cost_ext
    return "The total cost of your extra cleaning is: $" + str(Person1Estimate.total_cost_ext)
Person1Estimate =  Estimate(brnumber, bathnumber, kitchen, regService, sqftnumber, pets, frequency, full_cost)
#Person1ExtraServices = xtraServices(interior_windows, fridge, oven, blinds)
print(estimate(Person1Estimate))
#print(extraServicesfunct(Person1ExtraServices))
print("The total cost of your servicing with the standard and extra services will be: $" + str(Person1Estimate.full_cost))
runAnother = input("Would you like to run another estimate?")
print(runAnother)
if runAnother == "Y" or "y":
    print(estimate(Person2))
