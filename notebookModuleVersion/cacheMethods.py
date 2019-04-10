# Caching

def cacheRoutes(airportsInRoute,plane,cost,dictCache):
    ''''''
    #This first line will take the first aiport and store it as a variable
    firstAirport = airportsInRoute[0]
    #The next line gets the other remaining airports
    middleAirports = airportsInRoute[1:-1]
    #These next two lines append the plane and cost, so the middleAirports list contains the airports in the route
    #not including the first one, the plane used on the route, and the cost.
    middleAirports.append(plane)
    middleAirports.append(str(cost))
    #This adds the aforementioned list to a dictionary with the first airport as the key
    dictCache[firstAirport] = middleAirports


# In[49]:


def checkCache(airportList, myCache):
    ''''''
    #Go into this section if the cache dictionary actually has something in it
    if len(myCache) != 0:
        for i in myCache:
            #check if the first airport in the route matches any keys in the cache dictionary
            if airportList[0] == i:
                #If they do match, now convert the airport list you passed in (which will be the input the user
                #has provided) to a set, and then convert the cache's airports to a set and compare the two. This
                #is because the set ADT allows for comparison even if the order of the two sets do not match.
                #We also check if the planes of both routes match.
                if set(airportList[1:-1]) == set(myCache[i][0:-2]) and airportList[-1].rstrip() == myCache[i][-2]:
                    #If these conditions are met, we build a list with the first airport at the beginning, the middle
                    #airports as the next ones, and then the first one at the end again since the plane returns. We
                    #also append the cost to the list. The main code block will handle parsing the list to display results.
                    myReturn = [str(i)]
                    myReturn.extend(myCache[i][0:4])
                    myReturn.append(str(i))
                    myReturn.append(str(myCache[i][5]))
                    return myReturn
                else:
                    return False
    return False