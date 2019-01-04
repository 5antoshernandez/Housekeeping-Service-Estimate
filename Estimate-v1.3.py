
#######
#Notes#
#######

###################################
#Object code#######################
###################################
class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
class Estimate:
    def __init__(self, nameCreation):
        self.brnumber = int(input("How many bedrooms?"))
        self.bathnumber = float(input("How many bathrooms?"))
        self.sqftnumber = int(input("Sqft of your house?"))
        self.kitchen = input("Will you be needing your kitchen cleaned? \n Y for Yes\n N for no.")
        self.pets = str(input("Do you have pets? \n Y for Yes\n N for no."))
        self.frequency = input("How frequent will you be needing services?\n Please enter one of the following: \n weekly \n biweekly \n monthly \n onetime")
        self.full_cost = 0

###############################
#Method creation for estimate##
###############################
    def estimate(self):
        total_cost = 0
        ### adding cost of bedrooms and bathrooms
        total_cost += (10 * self.brnumber)
        total_cost += (20 * self.bathnumber)

        #Frequency conditionals
        if self.frequency == "weekly":
            total_cost = -5
        if self.frequency == "biweekly":
            print("By choosing biweekly, you saved $20 on your monthly bill!")
        if self.frequency == "monthly":
            total_cost += 10
            print("By choosing monthly, you saved $10 on your monthly bill!")
        if self.frequency == "onetime":
            total_cost += 30

        #Additional options considered by each household.
        if self.sqftnumber > 2000:
            total_cost = (self.sqftnumber * .05)
        elif self.sqftnumber > 500:
            total_cost = (self.sqftnumber - 500) * .07
        if self.kitchen == "Y" or self.kitchen == "y":
            total_cost += 25
        if self.pets == "Y" or self.pets == "y":
            total_cost += 25

        #Extra Services  conditionals
        extraServices = input("Are you interested in extra services?")
        if extraServices == "Y" or extraServices == "y":
            print("Running extra services!")
            self.extraServicesfunct()
        specialCleaning = input("Please input any special cleaning needs, if none, enter N or n.")
        if specialCleaning == "y" or specialCleaning == "Y":
            self.specialServicesfunct()
        self.full_cost += total_cost
        return "Your estimate will be between: " + "$" + str(round(self.full_cost - 10, 2)) + " - " + "$" + str(round(self.full_cost + 10, 2))


    def extraServicesfunct(self):
        total_cost_ext = 0
        interior_windows = input("Would you like your interior windows cleaned?")
        if interior_windows == "Y" or interior_windows == "y":
            how_many_windows = int(input("How many windows do you have?"))
            total_cost_ext += 7.5 * how_many_windows
        fridge = input("Would you like your fridge cleaned?")
        if fridge == "Y" or fridge == "y":
            total_cost_ext += 35
        oven = input("Would you like your oven cleaned?")
        if oven == "Y" or oven == "y":
            total_cost_ext += 45
        blinds = input("Would you like your blinds cleaned?")
        if blinds == "Y" or blinds == "y":
            total_cost_ext += 30
        self.full_cost += total_cost_ext
        return "The total cost of your extra cleaning is: $" + str(total_cost_ext)

    def specialServicesfunct(self):
        specialCleaningCost = 0
        whichSpecialService = input("Which special service will you be needing? \n Please choose from the following:\n Heavy Duty \n Deep Cleaning \n MIMO for Move-in Move-out \n PC for Post Construction \n Commercial")
        if whichSpecialService == "heavy duty" or whichSpecialService == "Heavy Duty":
            specialCleaningCost += 50
        if whichSpecialService == "Deep Cleaning" or whichSpecialService == "deep cleaning":
            self.full_cost = self.full_cost
        if whichSpecialService == "MIMO" or whichSpecialService == "mimo":
            return "Must do an in-person estimate."
        if whichSpecialService == "PC" or whichSpecialService == "pc":
            return print("Must do an in-person estimate.")
        if whichSpecialService == "Comm" or whichSpecialService =="comm":
            return "Must do in-person estimate."
        self.full_cost += specialCleaningCost
        return print("The total cost of your special cleaning is: $" + str(specialCleaningCost))

####################################
#Object creation and function call.#
####################################
def createEstimate():
    firstname = input("What is the client's first name?")
    lastname = input("What is the client's last name?")
    nameCreation= Name(firstname, lastname)
    estimateCreation = Estimate(nameCreation)
    print(estimateCreation.estimate())
    runAnother = input("Would you like to run another estimate?")
    if runAnother == "Y" or runAnother == "y":
        createEstimate()
    else:
        return ("Done!")
#####################
#First Estimate Call#
#####################
runEstimate = input("Would you like to run an estimate?")
if runEstimate == "Y" or runEstimate == "y":
    createEstimate()
