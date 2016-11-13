import csv

class Point(object):
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def print_point(self):
		test = str(self.x) + " " + str(self.y)
		print test 

with open('locations.csv', 'rb') as f:
	
	reader = csv.reader(f)
	building_names = {}

	for row in reader:
		point = Point(row[1], row[2])
		name = row[0].lower()
		building_names[name] = point 
	f.close()