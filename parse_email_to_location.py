#given raw string for email content 'a'
import imaplib
import sys
import email
import re

from building_dir_sym_tabl import building_names
from plot_location import plot 


FOLDER='Inbox'
LOGIN='freefoodmapprinceton@gmail.com'
PASSWORD='princetonfood'
IMAP_HOST = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(IMAP_HOST)
mail.login(LOGIN, PASSWORD)

mail.select()

typ, data = mail.search(None, 'SUBJECT', "FreeFood")
for num in data[0].split():
	result, email_data = mail.fetch(num, '(RFC822)')

	msg = email.message_from_string(email_data[0][1])
	
	subject = msg['subject']
	body = ""
	print 'Raw Date:', msg['Date']

	for part in msg.walk():
		if part.get_content_type() == 'text/plain':
			body = part.get_payload()

	txt = " " + subject + " " + body + " "
	#print txt 
	contents = txt.lower()

	timestamp = 60

	for key,value in building_names.items():
		i = contents.find(key)
		if i != -1 :
			plot(value, timestamp) 
			print key 

    	#value.print_point()


mail.close()
mail.logout()

