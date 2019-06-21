import email
import imaplib #imap pop
from bs4 import BeautifulSoup

import os
import mimetypes
username = 'your_email_id'
password = 'your_password'

mail = imaplib.IMAP4_SSL("imap.gmail.com") # https://www.google.com/settings/security/lesssecureapps
mail.login(username, password)

mail.select("inbox")

#Create new folder
# mail.create("Item2")

#list Folders
#mail.list()

result, data = mail.uid('search', None, "ALL") 

inbox_item_list = data[0].split()
result2, email_data = mail.uid('fetch', inbox_item_list[-1], '(RFC822)')
raw_email = email_data[0][1]
email_message = email.message_from_string(raw_email)
to_ = email_message['To']
from_ = email_message['From']
subject_ = email_message['Subject']
date_ = email_message['date']
counter = 1
for part in email_message.walk():
    if part.get_content_maintype() == "multipart":
        continue 
    filename = part.get_filename()
    content_type = part.get_content_type()
    if not filename:
        ext = mimetypes.guess_extension(content_type)
        if not ext:
            ext = '.bin'
        if 'text' in content_type:
            ext = '.docx'
        elif 'html' in content_type:
            ext = '.html'
        filename = 'msg-part-%08d%s' %(counter, ext)
    counter += 1
    #save file
save_path = os.path.join(os.getcwd(), "emails", date_, subject_)
if not os.path.exists(save_path):
    os.makedirs(save_path)
with open(os.path.join(save_path, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))


    # print (subject_)
    # print (content_type)
    # if "plain" in content_type:
    #   print(part.get_payload())
    # elif "html" in content_type:
    #   html_ = part.get_payload()
    #   soup = BeautifulSoup(html_ , "html.parser")
    #   text = soup.get_text()
    #   print(text)   
    # else:
    #   print(content_type)s	# print (subject_)
	# print (content_type)
	# if "plain" in content_type:
	# 	print(part.get_payload())
	# elif "html" in content_type:
	# 	html_ = part.get_payload()
	# 	soup = BeautifulSoup(html_ , "html.parser")
	# 	text = soup.get_text()
	# 	print(text)	  
	# else:
	# 	print(content_type)
