##COSTING
#Calculating the Cost of each leg
#
# Time complexity: O(n^2)


def findLegCosts(leg_distance_dict, airport_object_dict):
    """Takes in leg dictionary and airport objects. For each leg, it takes the departure airport
    and gets the local currency conversion rate. It then multiplies it by the distance to get the cost of each leg.
    Returns a dictionary with the cost of each leg."""
    costDict = {}
    for i in leg_distance_dict:
        myKey = i[:3]
        x = 0
        for j in airport_object_dict:
            if myKey == j:
                cost = round(float(airport_object_dict[j].exchange_rate) * float(leg_distance_dict[i]), 2)
                costDict[i] = cost
            x += 1
    return costDict


# ### Calculating the Cost of each Rotue
#
# Time complexity: O(n^2)



def findRouteCost(myList, costDict):
    """This returns the total cost of each route - using the cost of each leg. Returned in a dictionary
    with: Key: route(tuple) & Values: Total cost"""
    routeCostDict = {}
    x = 0
    while x < len(myList):
        i = 0
        cost = 0
        while i < (len(myList[x]) - 1):
            myKey = str(myList[x][i]) + "_" + str(myList[x][i + 1])
            cost += costDict[myKey]
            cost = round(cost, 2)
            i += 1
        routeCostDict[tuple(myList[x])] = cost
        x += 1
    return routeCostDict