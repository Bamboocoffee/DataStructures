##COSTING
#Calculating the Cost of each leg
#
# Time complexity: O(n^2)


def findRouteCost(list_of_route_lists, costDict):
    """This returns the total cost of each route - using the cost of each leg. Returned in a dictionary
    with: Key: route(tuple) & Values: Total cost"""
    routeCostDict = {} # create dictionary to store total route costs
    x = 0
    while x < len(list_of_route_lists): #loop through outer lists
        i = 0
        cost = 0
        while i < (len(list_of_route_lists[x]) - 1): # loop through inner list
            myKey = str(list_of_route_lists[x][i]) + "_" + str(list_of_route_lists[x][i + 1]) # connect first and second leg of route in format "DUB_LHR"
            cost += costDict[myKey] #find cost in dictionary of costs for each leg
            cost = round(cost, 2) #round to nearest 2nd decimal place
            i += 1
        routeCostDict[tuple(list_of_route_lists[x])] = cost # add tuple route list as key, value being cost
        x += 1
    return routeCostDict 


# ### Calculating the Cost of each Rotue
#
# Time complexity: O(n^2)

def findLegCosts(leg_distance_dict, airport_object_dict):
    """Takes in leg dictionary and airport objects. For each leg, it takes the departure airport
    and gets the local currency conversion rate. It then multiplies it by the distance to get the cost of each leg.
    Returns a dictionary with the cost of each leg."""
    costDict = {} #create dictionary to store leg costs
    for i in leg_distance_dict:
        try:
            myKey = i[:3] #strip out first three letters, which will be home airport's code (ex: DUB)
        except IndexError:
            print("There's an error in how the dictionary is built! Each key of the leg distance dict should have 'DUB_LHR' style formatting. The program will now fail.")
        for j in airport_object_dict:
            if myKey == j: #if key is in dictionary
                cost = round(float(airport_object_dict[j].exchange_rate()) * float(leg_distance_dict[i]), 2) # multiply exchange rate and distance of airport object, which is value for key
                costDict[i] = cost #add to new dictionary, with same key as leg_distance_dict
    return costDict