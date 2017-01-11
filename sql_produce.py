import parse_kc

f=open('tbl_create.sql','r')
s=''
while True :
       i = f.readline()
       s+=i
       if i=='': break
f.close()



User_data=parse_kc.user()   #List of Lists
Album_data=parse_kc.album()
Contain_data=parse_kc.contain()
Photo_data=parse_kc.photo()
s1=""
for i in User_data:
	s1=s1+"INSERT INTO User (username, firstname, lastname, password, email) VALUES ( '"+"','".join(str(items) for items in i)+"');\n"
		
s2=""
for i in Album_data:
	s_temp=	str(i[0])+",'"+ str(i[1])+"',"+','.join(str(items) for items in i[2:4])+",'"+ str(i[4])+"'"
	s2=s2+"INSERT INTO Album (albumid, title, created, lastupdated, username) VALUES ("+s_temp+");\n"

s3=""
for i in Contain_data:
	s_temp=",".join(str(items) for items in i[0:2])+",'"+"','".join(str(items) for items in i[2:])+"'"
	s3=s3+"INSERT INTO Contain (sequencenum, albumid, picid, caption) VALUES ("+s_temp+");\n"

s4=""
for i in Photo_data:
	s_temp=	"'"+str(i[0])+"','"+ str(i[1])+"',"+str(i[2])
	s4=s4+"INSERT INTO Photo (picid, format, date) VALUES ("+s_temp+");\n"


f=open('sql/tbl_create.sql','w')
f.write(s+s1+s2+s4+s3)
f.close()
