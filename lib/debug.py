#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1= Visitor('tyler')
    v2= Visitor('max')
    v3= Visitor('harry')
    v4= Visitor('ronaldo')

    p1= NationalPark('grand canyon')
    p2= NationalPark('mansuk')
    p3= NationalPark('CENTRAL')
    p4= NationalPark('dulles')

    t1 = Trip(v1, p1, 'jan 1st', 'jan 4th')
    t2 = Trip(v2, p1, 'jan 1st', 'jan 4th')
    t3 = Trip(v2, p1, 'jan 1st', 'jan 4th')
    t4 = Trip(v1, p1, 'jan 1st', 'jan 4th')





    ipdb.set_trace()
