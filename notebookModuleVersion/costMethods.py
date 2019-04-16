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



def checkAircraftAllowed(dictAirplane, distanceDict, input_list):
    """Checks that the aircraft being used can do the route. Returns the routes that are
    only possible with the aircraft"""
    planeToFly = input_list[5]
    planeRange = dictAirplane[planeToFly].max_capacity
    distanceDict_copy = distanceDict.copy()
    for j in distanceDict_copy:
        if distanceDict_copy[j] < int(planeRange):
            distanceDict.pop(j)
    finalRouteDict_copy = finalRouteDict.copy()
    for i in finalRouteDict_copy:
        toRemove = False
        for j in distanceDict:
            x = 0
            while x < len(i) - 1:
                if str(i[x] + "_" + i[x + 1]) == j:
                    toRemove = True
                x += 1
        if toRemove:
            finalRouteDict.pop(i)