# parse_data.py
import hashlib
import os

# User - username, firstname, lastname, password, email
def user():
	user = []
	user.append(['sportslover','Paul','Walker','paulpass93','sportslover@hotmail.com'])
	user.append(['traveler','Rebecca','Travolta','rebeccapass15','rebt@explorer.org'])
	user.append(['spacejunkie','Bob','Spacey','bob1pass','bspace@spacejunkies.net'])
	return user

# album - albumid, title, created, lastupdated, username
def album():
	album = []
	album.append(['1','I love sports','','','sportslover'])
	album.append(['2','I love football','','','sportslover'])
	album.append(['3','Around The World','','','traveler'])
	album.append(['4','Cool Space Shots','','','spacejunkie'])
	return album

# Contain - sequencenum, albumid, picid, caption
def contain():
	image_names = [ filename for filename in os.listdir('images')]
	albumid_lst = [2]*4 + [4]*5 + [1]*8 +[3]*13
	contain =[];
	for i,im_name in enumerate(image_names):
		albumid = albumid_lst[i]
		ptype = im_name.split('.')[1]
		m = hashlib.md5((str(albumid) + im_name).encode('utf-8'))
		contain.append([i,albumid,m.hexdigest(),''])
		#print i, albumid, im_name
	return contain

# Photo - picid, format, date
def photo():
	image_names = [ filename for filename in os.listdir('images')]
	albumid_lst = [2]*4 + [4]*5 + [1]*8 +[3]*13
	photo =[];
	for i,im_name in enumerate(image_names):
		albumid = albumid_lst[i]
		ptype = im_name.split('.')[1]
		m = hashlib.md5((str(albumid) + im_name).encode('utf-8'))
		photo.append([m.hexdigest(),ptype,''])
		#print i, albumid, im_name
	return photo







