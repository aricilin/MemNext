
from seed import Seed
import csv
import json



class SeedFile:
    def __init__(self, filename=None):
        self.filename = filename
        self.data = []

    def read_csv(self):
        with open(self.filename, "r") as f:
            #use of delimeters, can't handle comas otherwise 
            reader = csv.reader(f, delimiter=",")
            headers = next(reader)
            self.headers = headers
            for row in reader:
                # cast quality column to int
                # can get better
                row[0] = int(row[0])
                self.data.append(Seed(*row))


# To add more grains


    def write_csv(self):
        with open(self.filename, mode='w', newline='') as csv_file:
            fieldnames = ['quality', 'spectrum', 'code', 'key', 'index', 'name',
                          'definition', 'begin', 'end', 'place', 'author', 'location',
                          'time', 'right', 'join']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for seed in self.data:
                writer.writerow(seed.__dict__)




# reading from a json file

    def read_json(self):
        with open(self.filename, mode='r') as json_file:
            data = json.load(json_file)
            for seed in data:
                self.data.append(Seed(**seed))
# writing to a json file

    def write_json(self):
        with open(self.filename, mode='w') as json_file:
            json.dump([seed.__dict__ for seed in self.data], json_file)              