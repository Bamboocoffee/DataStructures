from math import pi, sin, cos, acos, floor

# Calculating all Route Permutations
#
# Time complexity: O(n)

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


def allPerms(listx):
    """ Creates permutations of all possible routes using the input list of airports and plane """

    a = listx[0]  # takes the departure airport
    permutation_list = listx[1:-1]  # creates a list that removes the departure airport and the aircraft

    count = 0
    permlist = []
    newpermlist = []
    perm = permutation(permutation_list)
    for i in list(perm):
        permlist.append(i)

    for perms in permlist:
        perms = [a] + list(perms) + [a]
        newpermlist.append(perms)

    return newpermlist


#Calculates distances between each airport pair
#
# Time complexity: n^4

def distanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
    radius_earth = 6371  # km
    theta1 = longitude1 * (2 * pi) / 360
    theta2 = longitude2 * (2 * pi) / 360
    phi1 = (90 - latitude1) * (2 * pi) / 360
    phi2 = (90 - latitude2) * (2 * pi) / 360
    distance = acos(sin(phi1) * sin(phi2) * cos(abs(theta1 - theta2)) + cos(phi1) * cos(phi2)) * radius_earth
    return floor(distance)


# In[42]:


def leg_distance_calculator(listx, airport_list):
    """Takes list of route and aircraft required. Also takes in dictionary of airport objects. Creates permutation
    list of airports. Using the objects passed, it finds the distance between each airport and saves the leg
    and distance as a key and value in a dictionary"""

    a = listx[0]  # takes the departure airport
    permutation_list = listx[1:-1]  # creates a list that removes the departure airport and the aircraft

    count = 0
    permlist = []
    perm = permutation(permutation_list)
    for i in list(perm):
        permlist.append(i)

    airport_distances = {}

    for perms in permlist:
        perms = [a] + list(perms) + [a]
        for i in range(0, len(perms) - 1):
            for j in airport_list:
                if j == perms[i]:
                    airport1 = airport_list[perms[i]]
                    for k in airport_list:
                        if k == perms[i + 1]:
                            airport2 = airport_list[perms[i + 1]]
                    distance = distanceBetweenAirports(float(airport1.longitude), float(airport1.latitude),
                                                       float(airport2.longitude), float(airport2.latitude))
                    if distance != 0:
                        airport_distances['_'.join([airport1.airport_code, airport2.airport_code])] = distance

    return airport_distances

