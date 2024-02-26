# INF360 - Programming in Python
# Jordin Myers
# Assignment 3

# [x] (1/1 points) Initial Comments.
# [x] (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
# [x] (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
# [x] (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
# [x] (5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
# [x] (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.
# (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

Ka = {
    "Name": "Ka",
    "Year Introduced": 1996, 
    "Production of the Current Model": 2014, 
    "Generation": 3, 
    "Vehicle Information": "Developed by Ford Brazil as a super mini car"
}
Fiesta = {
    "Name": "Fiesta",
    "Year Introduced": 1976,
    "Production of the Current Model": 2017,
    "Generation": 7,
    "Vehicle Information": "Ford's long running subcompact line based on global B-car Platform"
}
Focus = {
    "Name": "Focus",
    "Year Introduced": 1998,
    "Production of the Current Model": 2018,
    "Generation": 3,
    "Vehicle Information": "Ford's Compact car based on global C-car platform"
}
Mondeo = {
    "Name": "Mondeo",
    "Year Introduced": 1992,
    "Production of the Current Model": 2014,
    "Generation": 5,
    "Vehicle Information": 'Mid sized passenger sedan with "One-Ford" design based on CD4 platform'
}
Fusion = {
    "Name": "Fusion",
    "Year Introduced": 2005,
    "Production of the Current Model": 2014,
    "Generation": 5,
    "Vehicle Information": "Similar to Mondero"
}
Taurus = {
    "Name": "Taurus",
    "Year Introduced": 1986,
    "Production of the Current Model": 2009,
    "Generation": 6,
    "Vehicle Information": "Full sized car based on D3 platform"
}
FiestaST = {
    "Name": "Fiesta ST",
    "Year Introduced": 2013,
    "Production of the Current Model": 2013,
    "Generation": 1,
    "Vehicle Information": "Fiesta's high performance factory tune"
}
FocusRS = {
    "Name": "Focus RS",
    "Year Introduced": 2015,
    "Production of the Current Model": 2015,
    "Generation": 1,
    "Vehicle Information": "Special high performance Focus developed by SVT"
}
Mustang = {
    "Name": "Mustang",
    "Year Introduced": 1964,
    "Production of the Current Model": 2014,
    "Generation": 6,
    "Vehicle Information": "Ford's long running pony/muscle car"
}
GT = {
    "Name": "GT",
    "Year Introduced": 2004,
    "Production of the Current Model": 2016,
    "Generation": 2,
    "Vehicle Information": "Ford's limited production super car inspired by the legendary race car GT40"
}

cars = [Ka, Fiesta, Focus, Mondeo, Fusion, Taurus, FiestaST, FocusRS, Mustang, GT]

def nameDictionary(t):
    carDictionary = {}
    for i in t:
        carDictionary[i["Name"]] = i
        print(i["Name"] + ":", i)
    return carDictionary

def carNames(t):
    carList = []
    for i in t:
        carList.append(i["Name"])
    carList.sort()
    return carList

def carNamesAndYears(t):
    carDictionary = {}
    yearIntroduced = {}
    for i in t:
        carDictionary[i["Name"]] = i["Year Introduced"]
    return carDictionary

def yearIntroduced(t):
    yearIntroduced = {}
    for i in t:
        yearIntroduced[i["Year Introduced"]] = i["Name"]
    for i in sorted(yearIntroduced):
        print(i, ":", yearIntroduced[i])
    return yearIntroduced

print(nameDictionary(cars))
#print(carNames(cars))
#print(carNamesAndYears(cars))
yearIntroduced(cars)