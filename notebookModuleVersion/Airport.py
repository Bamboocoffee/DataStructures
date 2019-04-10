# Building Airport Objects
#
# Time complexity: 2n^2 + 4n ----> O(n^2)

# **Airport class**: Similar to the aircraft, each airport that is needed in the program is instantiated and is variables, airport code, longitutde, latitude and the exchange rate from euro is passed.
class Airport:

    def __init__(self, airport_code, longitude, latitude, exchangeRate):
        self.airport_code = airport_code  # airport code of the airport
        self._longitude = longitude  # longitude of the airport
        self._latitude = latitude  # latitude of the airport
        self._exchange_rate = exchangeRate  # currency used by the airport

    @property
    def longitude(self):
        return self._longitude  # returns the longitude of the airport

    @property
    def latitude(self):
        return self._latitude  # returns the latitude of the airport

    @property
    def exchange_rate(self):
        return self._exchange_rate  # returns the currency used by the airport

    @exchange_rate.setter
    def exchange_rate(self, exchangeRate):
        self._exchange_rate = exchangeRate  # sets the currency of the airport

