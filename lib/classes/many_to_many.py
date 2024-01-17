class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >=3 and not hasattr(self, 'name'):
            self._name = name
           
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        all_visitors = [trip.visitor for trip in self.trips()]
        if all_visitors:
            return max(set(all_visitors), key = all_visitors.count)
        else:
            return None
    @classmethod
    def most_visited(cls):
        return max(cls.all, key= lambda park:park.total_visits())
        
        


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value
    
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
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
        return [trip for trip in Trip.all if trip.visitor ==self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        visits = [trip for trip in self.trips() if trip.national_park == park]
        print(visits)
        if visits:

            return len(visits)
        else:
            return 0
# ipdb.set_trace()