import ipdb
class NationalPark:
    all=[]
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    # in visitiros() list which contains all visitors that visited particular
    #park, 
    def visitors(self):
        print([trip.visitor for trip in self.trips()])
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        if len(self.trips()):
            return len(self.trips())
        
    def best_visitor(self):
        all_visitors = [trip.visitor for trip in self.trips()]
        unique_visitors = set(all_visitors)
        most_occuring_visitor = max(unique_visitors, key=all_visitors.count)
        return most_occuring_visitor

    #labmda function syntax = giving most visited park
    @classmethod  
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits()) 
        # not made into set because
    #cls.all list contains unique instances of national parks - total visits number of visits
    #particular park was visited. so finding most visited park instance based on number of visits


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        

    

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
    
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
        
    # get list of visitor's trips. create a list of visitors's park visited
    #sum it up 
    def total_visits_at_park(self, park):
        given_park_visited_freq = [trip.national_park for trip in Trip.all if trip.national_park == park and trip.visitor == self]
        return len(given_park_visited_freq)
park1 = NationalPark('grand canyon')
park2 = NationalPark('central park')
visitor1 = Visitor('tyler')
visitor2 = Visitor('John')
visitor3 = Visitor('Jamie')
trip1 = Trip(visitor1, park1, "September 1st", "September 3rd" )
trip3 = Trip(visitor1, park2, "September 1st", "September 3rd" )
trip5 = Trip(visitor1, park1, "September 1st", "September 3rd" )
trip4 = Trip(visitor1, park2, "September 1st", "September 3rd" )
trip2 = Trip(visitor2, park2, "December 4t", "January 16th" )
trip2 = Trip(visitor3, park1, "December 4t", "January 16th" )
trip6 = Trip(visitor2, park1, "December 4t", "January 16th" )
# print(park1, park2, visitor1, trip2)
visitor1.name = 'Tyler Kim'
# ipdb.set_trace()
