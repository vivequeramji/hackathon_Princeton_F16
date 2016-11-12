import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def plot(place, time):
	#size = time.time - time
	#alp = 0.5 #+ (size/7200.0)
	alp = 1000
	plt.scatter(x=place.x, y=place.y, alpha=alp)



fname = 'map.jpg'
image = Image.open(fname)
arr = np.asarray(image)
plt.imshow(arr)

plt.scatter([1500], [1500], alpha=0.5)

# put a red dot, size 40, at 2 locations:


plt.show()