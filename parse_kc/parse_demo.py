import parse_kc

# return user info (3) - [username, firstname, lastname, password, email]
print 'user:', parse_kc.user(),'\n'

# return album info (4) - [albumid, title, created, lastupdated, username]
# need to add 'created' & 'lastupdated'
print 'album:', parse_kc.album(),'\n'

# return contain info (30) - [sequencenum, albumid, picid, caption]
print 'contain:', parse_kc.contain(),'\n'

# return photo info (30) - [picid, format, date]
# need to add 'date'
print 'photo:', parse_kc.photo(),'\n'

