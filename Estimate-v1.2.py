#oven = 45
#heavy_duty = 50
#fan = 5
#deep cleaning = 2 * regular_price
#movein_moveout =
###################################################################
#Our user inputs to input into initalize an instance of an object.#
###################################################################

#Consider moving inputs into the constructor itself that way each time a new instance is constructed they will be called and saved.
full_cost = 0
brnumber = input("How many bedrooms?")
bathnumber = input("How many bathrooms?")
sqftnumber = input("Sqft of your house?")
pets = input("Do you have pets? Y for Yes, N for no.")
frequency = input("How frequent will you be needing services?")
kitchen = input("Will you be needing your kitchen cleaned? Y for Yes, N for No.")
#specialCleaning = input("Please input any special cleaning needs, if none, enter N or n.")



###################################
#Object code#######################
###################################
class Estimate:
    def __init__(self, brnumber, bathnumber, kitchen, sqftnumber, pets, frequency, full_cost):

        self.brnumber = int(brnumber)
        self.bathnumber = float(bathnumber)
        self.kitchen = str(kitchen)
        self.sqftnumber = int(sqftnumber)
        self.pets = str(pets)
        self.frequency = frequency
        self.full_cost = full_cost
        #self.specialCleaning = specialCleaning

###############################
#Method creation for estimate##
###############################
    def estimate(object):
        total_cost = 0
        ### adding cost of bedrooms and bathrooms
        total_cost += (10 * object.brnumber)
        total_cost += (20 * object.bathnumber)

        #Frequency conditionals
        if object.frequency == "weekly":
            total_cost = -5
        if object.frequency == "biweekly":
            print("By choosing biweekly, you saved $20 on your monthly bill!")
        if object.frequency == "monthly":
            total_cost += 10
            print("By choosing monthly, you saved $10 on your monthly bill!")
        if object.frequency == "onetime":
            total_cost += 30

        #Additional options considered by each household.
        if object.sqftnumber > 500:
            total_cost = (object.sqftnumber - 500) * .07
        if object.kitchen == "Y" or object.kitchen == "Y" "y":
            total_cost += 25
        if object.pets == "Y" or object.pets == "y":
            total_cost += 25

        #Extra Services  conditionals
        extraServices = input("Are you interested in extra services?")
        if extraServices == "Y" or extraServices == "y":
            print("Running extra services!")
            object.extraServicesfunct()
        object.full_cost += total_cost
        return "Your estimate will be between: " + "$" + str(object.full_cost - 10) + " - " + "$" + str(object.full_cost + 10)


    def extraServicesfunct(object):
        total_cost_ext = 0
        print("Extra Function Called!")
        interior_windows = input("Would you like your interior windows cleaned?")
        blinds = input("Would you like your blinds cleaned?")
        fridge = input("Would you like your fridge cleaned?")
        oven = input("Would you like your oven cleaned?")
        if interior_windows == "Y" or interior_windows == "y":
            how_many_windows = int(input("How many windows do you have?"))
            total_cost_ext += 7.5 * how_many_windows
        if fridge == "Y" or fridge == "y":
            total_cost_ext += 35
        if oven == "Y" or oven == "y":
            total_cost_ext += 45
        if blinds == "Y" or blinds == "y":
            total_cost_ext += 30
        object.full_cost += total_cost_ext
        return "The total cost of your extra cleaning is: $" + str(total_cost_ext)


####################################
#Object creation and function call.#
####################################
Person1Estimate = Estimate(brnumber, bathnumber, kitchen, sqftnumber, pets, frequency, full_cost)
print(Person1Estimate.estimate())
#print("The total cost of your servicing with the standard and extra services will be: $" + str(Person1Estimate.full_cost))
runAnother = input("Would you like to run another estimate?")
print(runAnother)
if runAnother == "Y" or "y":
    print(estimate(Person2))