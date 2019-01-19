import sqlite3
conn = sqlite3.connect('housekeeping.db')
curr = conn.cursor()

#######
#Notes#
#######
#Consider adding a billing table with a date, time, & fee with servicing as well.
#0 = False/No, 1 = True/Yes
#Special Services
####0 = Heavy Duty
####1 = Deep Cleaning
####2 = Move-in Move-out
####3 = Post Construction
####4 = Commercial

###################################
#Object code#######################
###################################
class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname
        #Initializes a Row in Clients Table.
        curr.execute('INSERT OR IGNORE INTO Clients (name) VALUES (?)', ( self.fullname, ))
        conn.commit()
class Estimate:
    def __init__(self, nameCreation):
        self.name = nameCreation.fullname
        self.address = input("What's the house's address?")
        self.brnumber = int(input("How many bedrooms?"))
        self.bathnumber = float(input("How many bathrooms?"))
        self.sqftnumber = int(input("Sqft of your house?"))
        self.kitchen = input("Will you be needing your kitchen cleaned? \n Y for Yes\n N for no.")
        self.pets = str(input("Do you have pets? \n Y for Yes\n N for no."))
        self.frequency = input("How frequent will you be needing services?\n Please enter one of the following: \n weekly \n biweekly \n monthly \n onetime")
        curr.execute('SELECT id FROM Clients WHERE name = ?', (nameCreation.fullname,))
        self.client_id = curr.fetchone()[0]
        #This either initializes the House table or Updates it if the address is already on file.
        try:
            curr.execute('''INSERT INTO House (address, bedrooms, bathrooms, sqft, pets, client_id) VALUES (?, ?, ?, ?, ?, ?)''', (self.address, self.brnumber, self.bathnumber, self.sqftnumber, self.pets, self.client_id))
        except:
            curr.execute('''UPDATE House SET address = ?, bedrooms = ?, bathrooms = ?, sqft = ?, pets = ? WHERE client_id = ?''', (self.address, self.brnumber, self.bathnumber, self.sqftnumber, self.pets, self.client_id))
        conn.commit()
        curr.execute('SELECT id FROM House WHERE client_id = ?', (self.client_id, ))
        self.house_id = curr.fetchone()[0]
        print(self.house_id)
        try:
            curr.execute('INSERT OR IGNORE INTO Clients house_id = ? WHERE name = ?', (self.house_id, self.name))
            conn.commit()
        except:
            curr.execute('''UPDATE Clients SET house_id = ? WHERE name = ?''', (self.house_id, self.name))
            conn.commit()
        #Updates the row of a particular house that the client is associated with.
        #May want to consider changing the WHERE clause to address instead of client_id.
        curr.execute('''UPDATE House SET kitchen = ?, frequency = ? WHERE client_id = ?''', (self.kitchen, self.frequency, self.client_id))
        conn.commit()
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
        #Updating the Fee in a particular House table.
        #May want to update by address in case the client is associated with
        #Multiple properties.
        curr.execute('UPDATE House SET (fee) = ? WHERE client_id = ?', (self.full_cost, self.client_id))
        conn.commit()
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
        #Updates the Row with extra services data if requested.
        curr.execute('''UPDATE House SET extra_services = ?, int_windows = ?, fridge = ?, oven = ?, blinds =? WHERE address = ?''', ("Y", interior_windows, fridge, oven, blinds, self.address))
        conn.commit()
        return "The total cost of your extra cleaning is: $" + str(total_cost_ext)

    def specialServicesfunct(self):
        specialCleaningCost = 0
        specialCleaningDBVar = None
        whichSpecialService = input("Which special service will you be needing? \n Please choose from the following:\n Heavy Duty \n Deep Cleaning \n MIMO for Move-in Move-out \n PC for Post Construction \n Commercial")
        if whichSpecialService == "heavy duty" or whichSpecialService == "Heavy Duty":
            specialCleaningCost += 50
            specialCleaningDBVar = 0
        if whichSpecialService == "Deep Cleaning" or whichSpecialService == "deep cleaning":
            specialCleaningCost = self.full_cost
            specialCleaningDBVar = 1
        if whichSpecialService == "MIMO" or whichSpecialService == "mimo":
            specialCleaningDBVar = 2
            return "Must do an in-person estimate."
        if whichSpecialService == "PC" or whichSpecialService == "pc":
            specialCleaningDBVar = 3
            return print("Must do an in-person estimate.")
        if whichSpecialService == "Comm" or whichSpecialService =="comm":
            specialCleaningDBVar = 4
            return "Must do in-person estimate."
        self.full_cost += specialCleaningCost
        #Updates the partciular row with special services data.
        curr.execute('UPDATE House SET special_services = ? WHERE client_id = ?', (specialCleaningDBVar, self.client_id))
        conn.commit()
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
