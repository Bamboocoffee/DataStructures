import Aircraft
import Airport
import csv

def buildAirports(listy):
    """Takes in a list of the route to be analysed. The airports are searched for in the csv.
    Objects of that airport are then created - with attributes latitude, longitude, and the exchange rate to Euro.
    It returns a dictionary with airport_code as key and object as value"""
    listx = listy[:-1]
    airport_list = []  # creates a new list

    with open('airport.csv', newline='', encoding="utf8") as airport_file:  # opens the csv file
        reader = csv.reader(airport_file)  # reads the cotents to a variable
        next(reader, None)  # returns none at the end of the file
        for airport in reader:  # iterates through the reader
            if airport[4] in listx:
                airport_code = airport[4]  # assigns variable
                country_name = airport[3]  # assigns variable
                longitude = airport[6]  # assigns variable
                latitude = airport[7]  # assigns variable
                templist = [airport_code, country_name, longitude, latitude]
                airport_list.append(templist)
    if (len(airport_list)) != 5:
        return False

    country_currency_list = []  # creates a new list

    with open('countrycurrency.csv', newline='', encoding="utf8") as countrycurrency_file:  # opens the csv file
        reader = csv.reader(countrycurrency_file)  # reads the cotents to a variable
        next(reader, None)  # returns none at the end of the file
        for country in reader:  # iterates through the reader
            temp_list = [country[0], country[14]]  # temp list created
            country_currency_list.append(temp_list)  # appends temp list to the main list

    currency_list = []  # creates a new list

    with open('currencyrates.csv', newline='', encoding="utf8") as currencyrates_file:  # opens the csv file
        reader = csv.reader(currencyrates_file)  # reads the cotents to a variable
        next(reader, None)  # returns none at the end of the file
        for currency in reader:  # iterates through the reader
            temp_list = [currency[1],currency[2]]  # temp list created
            currency_list.append(temp_list)  # appends temp list to the main list

    #Outer for loops goes through list of countries and the currency they have. Inner loop will go through currency
    #and exchange rate list, matches currency to exchange rate, and creates a final list of lists with the
    #country and currency rate in each inner list.
    final_list = []
    for i in country_currency_list:
        for x in currency_list:
            if i[1] == x[0]:
                templist = [i[0], x[1]]
                final_list.append(templist)

    #Outer for loop will go through list of lists that contains airport, country, latitude, longitude,
    #and the inner loop will go through the list of airports and currency information and then match
    #them with the airport in the outer list. The inner loop will then extend
    x = 0
    i = 0
    while x < len(airport_list):
        while i < len(final_list):
            if airport_list[x][1] == final_list[i][0]:
                airport_list[x].extend(final_list[i])
                break
            i+=1
        x+=1
    # Make a dictionary with the Airport code as the key and the value being the airport object of that key
    finalAirports = {}
    for i in airport_list:
        finalAirports[i[0]] = Airport.Airport(i[0], i[2], i[3], i[5])

    return finalAirports

def buildAircraft():
    """Builds objects for each of the aircraft - with attributes model, manufacturer, and range.
    Returns a dictionary of this"""
    aircraftDict = {}
    with open('aircraft.csv', newline='', encoding="utf8") as airplane_file:  # opens the csv file
        reader = csv.reader(airplane_file)  # reads the cotents to a variable
        next(reader, None)  # returns none at the end of the file
        for airplane in reader:  # iterates through the reader
            if airplane[2] == "imperial":
                airRange = int(airplane[4]) * 1.609
            else:
                airRange = airplane[4]
            aircraftDict[airplane[0]] = Aircraft.Aircraft(airplane[0], airplane[3], airRange)
    return aircraftDict

