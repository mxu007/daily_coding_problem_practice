# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute a possible itinerary,
# If no such itinerary exists, return null. All flights must be used in the itinerary

# E.g. Given the list of flights [('SFO', 'HKO'), ('YYZ','SFO'), ('YUL','YYZ'), ('HKO', 'ORD')] and starting airport 'YUL'
# Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

# can you construct a partial solution? -- incomplete itinerary and extend it by adding more flights
# can you verify if the partial solution is invalid -- solution is invalid if there are no flights leaving from last desitination and there are still flights remaining taht can be taken
# can you verify if the solution is complete -- yes, check if a solution is complete if our itinerary uses all the flights

# maintain a list represent current itinerary "current_itinerary". For each possible next flight, we try appending it to the current_itinerary and call the function recursively with reduced(leftover) flights. As long as we find a valid itinerary, we return the results. If we don't find any possible valid itinerary, we return None
# O(n!) time complexity, O(n) space for the itinerary list
# at step i, there will be i-1 continuation path to expolore... like n*(n-1)*(n-2)*...*1
def get_itinerary(flights, current_itinerary):
    # use up all the flights and we're done
    if not flights:
        return current_itinerary

    last_stop = current_itinerary[-1]

    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i+1:]
        # append possible destination to the last destination in current itinerary
        current_itinerary.append(destination)
        # if origin of newly appended flight match with the last stop, recursive call
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        
        # if not matched with last stop, pop this candidate, prune this path
        current_itinerary.pop()
    # no valid itinerary found, return None
    return None

if __name__ == "__main__":
    # flights is a list of tuples
    flights = [('SFO', 'HKO'), ('YYZ','SFO'), ('YUL','YYZ'), ('HKO', 'ORD')]
    current_itinerary = ['YUL']
    print(get_itinerary(flights,current_itinerary))

    print("--------------------------------------")

    flights = [('SFO','COM'),('COM','YYZ')]
    current_itinerary = ['COM']
    print(get_itinerary(flights,current_itinerary))