# Building the Aircraft
#
# Time complexity: O(n)

#  **Aircraft class:** This class builds the aircraft to be used. Each aircraft object is to be assigned the model, maundacturer, max capacity and the currency capacity of the aircraft. Approprite setters and getters are implemented in order to access the object variables later in the program.
# Below is a function that builds each of the aircraft.
class Aircraft:  # Class that contains all aircraft

    def __init__(self, model, manufacturer, max_capacity, current_capacity=0):
        self._model = model  # model of the aircraft
        self._manufacturer = manufacturer  # manufacturer of the aircraft
        self._max_capacity = max_capacity  # max capacity of the aircraft
        self._current_capacity = current_capacity  # current capacity of the aircraft

    @property
    def max_capacity(self):
        return self._max_capacity  # returns the max distance

    @property
    def manufacturer(self):
        return self._manufacturer  # returns the manufacturer

    @property
    def model(self):
        return self._model  # returns the model

    @property
    def current_capacity(self):
        return self._current_capacity  # returns the current capacity left in the plane

