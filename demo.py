##
 # Flightaware data scraper demo using veryprettytable
 #
 # @author      Nimrod Goldrat
 # @website     http://nimrod.goldrat.info
 # @copyright   Nimrod Goldrat 2014
 #
##

from flightaware.flightaware import flightaware
from veryprettytable import VeryPrettyTable

class demo(object):
    """flightaware demo"""
    def __init__(self, flight):
        super(demo, self).__init__()
        self.data, self.data2, self.flight_name = flightaware().get(flight)
        self.table_header = VeryPrettyTable()
        self.table_header.field_names = ['Flight info','Data']
        for v, k in self.flight_name.iteritems():
            self.table_header.add_row([v,k])
        self.table = self.create(self.data, self.data2)
        print self.table_header
        print self.table

    def create(self, departure, arrival):
        table = VeryPrettyTable()
        table.field_names = ['Departure',' ','Arrival','  ']
        for de,ar, in zip(departure,arrival):
            table.add_row([de,departure[de],ar,arrival[ar]])
        return table

import time
import os
while (True):
    b = demo("CPZ5859")
    time.sleep (60)
    os.system('cls' if os.name == 'nt' else 'clear')

