
from Seed import Seed
import csv
import json



class SeedSerializer:


    def __init__(self, filename=None, filename_links=None):
        self.filename = filename
        self.filename_links = filename_links

    def read(self):
        raise NotImplementedError("This is an unimplemented abstract method")

    def write(self):
        raise NotImplementedError("This is an unimplemented abstract method")
    
    def writeLinks(self):
        raise NotImplementedError("This is an unimplemented abstract method")




class CsvSerializer(SeedSerializer):
    def __init__(self, filename=None, filename_links=None):
        super().__init__(filename, filename_links)

    def read(self):
        seedList = []
        with open(self.filename, "r") as f:
            #use of delimeters, can't handle comas otherwise 
            reader = csv.reader(f, delimiter=",")
            headers = next(reader)
            self.headers = headers
            for row in reader:
                # cast quality column to int
                # can get better
                row[0] = int(row[0])
                seedList.append(Seed(*row))

# To add more grains

    def write(self, seedList):
        with open(self.filename, mode='w', newline='', encoding='utf8') as csv_file:
            fieldnames = ['quality', 'spectrum', 'code', 'key', 'index', 'name',
                          'definition', 'begin', 'end', 'place', 'author', 'location',
                          'time', 'right', 'join', '_position_start', '_position_end']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for seed in seedList:
                writer.writerow(seed.__dict__)
    
    def writeLinks(self, linkList):
        with open(self.filename_links, mode='w', newline='', encoding='utf8') as csv_file:
            fieldnames = ['seed1', 'seed2']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for link in linkList:
                writer.writerow({'seed1': link[0], 'seed2': link[1]})



class JsonSerializer(SeedSerializer):
    def __init__(self, filename=None, filename_links=None):
        super().__init__(filename, filename_links)


    def read(self):
        seedList = []
        with open(self.filename, mode='r') as json_file:
            data = json.load(json_file)
            for seed in data:
                seedList.append(Seed(**seed))


    def write(self, seedList):
        with open(self.filename, mode='w', encoding='utf8') as json_file:
            json.dump([seed.__dict__ for seed in seedList], json_file, ensure_ascii=False)              