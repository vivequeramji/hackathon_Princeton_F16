import time 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


TIME_CONSTANT = 3600*6

def plot(place, timestamp):

	size = time.time() - timestamp
	alp = 0.5 + (size/(2*TIME_CONSTANT))
	plt.scatter(x=place.x, y=place.y, s=150, alpha=alp)