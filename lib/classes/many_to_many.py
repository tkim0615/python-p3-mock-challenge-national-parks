class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name        
    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass


class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and (start_date.endswith('st') or start_date.endswith('nd') or start_date.endswith('rd') or start_date.endswith('th')):
            self._start_date = start_date


class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <=15:
            self._name = name
    
        
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass