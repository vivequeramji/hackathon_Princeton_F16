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

#testPoint = Point(1,2)
#testPoint.print_point()

'''
def make_point(x, y)
	point = Point(x,y)
	return point
'''
'''
testPoint = Point(1,2)
test = str(testPoint.x) + " " + str(testPoint.y)
print test 
'''

with open('buildingDirTest.csv', 'rb') as f:
	reader = csv.reader(f)

	building_names = {}

	next(f)
	for row in reader:
		point = Point(row[1], row[2])
		point.print_point()
		#name = row[0]
		building_names[row[0]] = point 
		#school_districts.append(row[3])
		#school_addresses.append(row[10] + " " + row[12])
	f.close()

for key,value in building_names.items():
    print key #+ " => " + value
    value.print_point()
