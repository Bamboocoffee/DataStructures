from math import pi, sin, cos, acos, floor

# Calculating all Route Permutations

#Time complexity is O(n!) as it iterates through all the permutations of the input list through recursion. 
def permutation(lst): #Calculates the different possible permutations of a given list.
    if len(lst) == 0: 
        return [] #There are no permutations if the list is empty.
    if len(lst) == 1: 
        return [lst] #There is only one possible permutation if there is only one item in the list.
    
    #If there is more than one item in the list, then the different permutations can be found.
    l = []  #This empty list will store the different possible permutations.
    
    for i in range(len(lst)):
        m = lst[i] #Take out the first item of the list.
        remLst = lst[:i] + lst[i + 1:] #remLst is the remaining list after taking out the first item.
        for p in permutation(remLst):
            l.append([m] + p) 
            #The possible permutations with m as the first item is appended into the new list. M increments after each iteration               until the length of the list is reached. 
    return l #new list with all possible permutations is returned. 

#Time complexity is O(n!) since it calls permutation function within allPerms function.
def allPerms(listx): #Creates permutations of all possible routes using the input list of airports and plane.
    
    a = listx[0]  # stores the departure airport (which is the first element of the list) in a variable.
    permutation_list = listx[1:-1]  # creates a new list that has removed the departure airport (var a) and the aircraft (last                                         element of the list).

    permlist = []
    newpermlist = []
    perm = permutation(permutation_list) #using permutation recursive function to find all the possible permutations from 2nd         element in listx to the 2nd last element in listx (permutation list). Each permutation list is appended to permlist. 
    for i in list(perm):
        permlist.append(i)

    for perms in permlist: #for each item in the permlist, the first element of listx is appended to the beginning and end and         stored in perms. Perms is then appended to newpermlist which has all the possible permutations with the first element in listx     being the departure airport and final arrival airport.
        perms = [a] + list(perms) + [a]
        newpermlist.append(perms)

    return newpermlist #the function returns the final permutation list with the first element in listx being the departure           airport and final arrival airport.


#Calculates distances between each airport pair

#Time complexity: O(1)
#Algorithm taken from practical class. 
def distanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
    radius_earth = 6371  # km
    theta1 = longitude1 * (2 * pi) / 360
    theta2 = longitude2 * (2 * pi) / 360
    phi1 = (90 - latitude1) * (2 * pi) / 360
    phi2 = (90 - latitude2) * (2 * pi) / 360
    distance = acos(sin(phi1) * sin(phi2) * cos(abs(theta1 - theta2)) + cos(phi1) * cos(phi2)) * radius_earth
    return floor(distance)



# Time complexity: O(n^4)
def leg_distance_calculator(listx, airport_list): #Takes list of route and aircraft requried. Takes in dictionary of airport objects. Creates permutation list of airports. Using the objects passed, it finds the distance between each airport and saves the leg and distance as a key and value in a dictionary. 

    airport_distances = {} #creates an empty dictionary to store each permutation pair and its distance.
    permlist = allPerms(listx) #generates the list of permutations from the input list with the first and last element of the n       permlist being the first element of listx.

    for perms in permlist:
        for i in range(0, len(perms) - 1): #iterates through each item in each list of the permlist.
            for j in airport_list:
                if j == perms[i]: #if an element in the airport list is equal to an iteration of the permlist, assign it to                                         airport 1.
                    airport1 = airport_list[perms[i]]
                    for k in airport_list: 
                        if k == perms[i + 1]: #if another element in the airport list is equal to an iteration of the permlist,                                                 assign it to airport 2.
                            airport2 = airport_list[perms[i + 1]]
                    #the longitude and latitude attribute of airport1 object are retrived and the longitude and latitude attribute                     of airport2 object are retrived. These values are used to calculate the distance between each airport object.
                    distance = distanceBetweenAirports(float(airport1.longitude), float(airport1.latitude),
                                                       float(airport2.longitude), float(airport2.latitude)) 
                    #if the distance is not equal to 0, append the distance value to airport_distances dictionary and use                             airport1+airport2 code as the key. 
                    if distance != 0:
                        airport_distances['_'.join([airport1.airport_code, airport2.airport_code])] = distance

    return airport_distances 

