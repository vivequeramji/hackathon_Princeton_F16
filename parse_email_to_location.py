import imaplib
import sys
import email
import re
import datetime
import time 
from email.utils import parsedate_tz, mktime_tz, formatdate

from building_dir_sym_tabl import building_names
from plot_location import plot, TIME_CONSTANT 

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

FOLDER='Inbox'
LOGIN='freefoodmapprinceton@gmail.com'
PASSWORD='princetonfood'
IMAP_HOST = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(IMAP_HOST)
mail.login(LOGIN, PASSWORD)

mail.select()

fname = 'map.jpg'
image = Image.open(fname)
arr = np.asarray(image)
plt.imshow(arr)

typ, data = mail.search(None, 'SUBJECT', "FreeFood")
a = data[0].split()
for num in reversed(a):
	result, email_data = mail.fetch(num, '(RFC822)')

	msg = email.message_from_string(email_data[0][1])
	
	subject = msg['subject']
	body = ""

	date = email.utils.parsedate_tz(msg['Date'])
	timestamp = mktime_tz(date)
	if (time.time() - timestamp) > TIME_CONSTANT:
		break

	for part in msg.walk():
		if part.get_content_type() == 'text/plain':
			body = part.get_payload()

	txt = " " + subject + " " + body + " "
	
	contents = txt.lower()

	for key,value in building_names.items():
		i = contents.find(key)
		if i != -1 :
			plot(value, timestamp) 

plt.show()
mail.close()
mail.logout()

