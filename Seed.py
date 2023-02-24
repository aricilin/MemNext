import re
from datetime import datetime


class Seed:
    def __init__(self=None, quality=0, spectrum=None, code=None, key=None, index=None, name=None,
                 definition=None, begin=None, end=None, place=None, author=None, location=None,
                 time=None, right=None, join=None):
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
        if quality not in range(10):
            raise ValueError("Quality must be an integer between 0 and 9")
        return quality

    # check the key and return true if valid
    def validate_key(self, key):
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