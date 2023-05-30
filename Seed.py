import re
from datetime import datetime


class Seed:
    def __init__(self=None, quality=0, spectrum=None, code=None, key=None, index=None, name=None,
                 definition=None, begin=None, end=None, place=None, author=None, location=None,
                 time=None, right=None, join=None, _position_start=None, _position_end=None):
        self.quality = self.validate_quality(quality)
        self.spectrum = spectrum
        self.code = code
        self.key = self.validate_key(key)
        self.index = index
        self.name = name
        self.definition = definition
        self.begin = self.validate_date(begin)
        self.end = self.validate_date(end)
        self.place = place
        self.author = author
        self.location = location
        self.time = time
        self.right = right
        self.join = join

        self._position_start = _position_start
        self._position_end = _position_end

    # to  visualise

    def __str__(self):
        return f"Seed(key='{self.key}', name='{self.name}')"

    # to set a property of the seed to specified value
    def set_property(self, property_name, property_value):
        setattr(self, property_name, property_value)

    # returns the value of a specified property of the seed
    def get_property(self, property_name):
        return getattr(self, property_name)

    # True if the Seed object has a specified property,
    def has_property(self, property_name):
        return hasattr(self, property_name)

    # To set relations between seeds
    def set_relationship(self, relationship_type, target_seed):
        if relationship_type == "right":
            self.right = target_seed
        elif relationship_type == "join":
            self.join = target_seed
    # eturns the related seed

    def get_relationship(self, relationship_type):
        if relationship_type == "right":
            return self.right
        elif relationship_type == "join":
            return self.join
        else:
            return None
    # returns True if the seed has the given relation

    def has_relationship(self, relationship_type):
        if relationship_type == "right":
            return self.right is not None
        elif relationship_type == "join":
            return self.join is not None
        else:
            return False

    # check the quality and return true if valid
    def validate_quality(self, quality):
        if quality != None:
            return quality
        if quality not in ["q1","q2", "q3", "q4","q5", "q6", "q7","q8", "q9", "q0"]:
            raise ValueError("Quality must be qX")
        return quality

    # check the key and return true if valid
    def validate_key(self, key):
        if key == None:
            return key
        if isinstance(key, str) and re.match(r'^[A-Za-z0-9_-]+$', key):
            return key
        else:
            raise ValueError(
                "Key must be a string. Only letters, numbers, are allowed.")

    # check the date and return true if valid
    def validate_date(self, date_str):
        if date_str is None:
            return None
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date().isoformat()
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD'.")



    def distance(self, seed):
        if  seed._position_start > self._position_end:
            return seed._position_start - self._position_end
        if self._position_start > seed._position_end:
            return self._position_start - seed._position_end
        return 0 