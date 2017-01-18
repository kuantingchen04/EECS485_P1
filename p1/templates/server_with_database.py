import socket
import os
import sys
import os,time
import sqlite3
mobile_directory="Files/mobile_files"
recycle_bin_directory='RecycleBin/'
db = sqlite3.connect('example.db')
c = db.cursor()
db.commit()

def decodeData(data):
    decodedStr2 = data.decode("utf-8",'replace')
    return decodedStr2

def openAndSendBackFile(imageName,connection):
    print 'Opening image ' + imageName
    imageFile = open(imageName,'rb')
    image_data = imageFile.read()
    print 'Sending image......'
    imageFile = open(imageName,'rb')
    while 1:
        image_data = imageFile.readline(1024)
        if not image_data:
            connection.send('/ENDOFFILE')
            break
        connection.send(image_data) 
    print 'Finished sending file'
def saveFile(imgName,connection):
    fp = open(mobile_directory+'/' + imgName,'wb')
    while 1:
        strng = connection.recv(1024)
        if not strng:
            break
        if '/ENDOFFILE' in strng:
            break
        fp.write(strng)
    fp.close()
    print 'finished receive file'
def PCsaveFile(imgName,connection):
    fp = open('Files/'+ imgName,'wb')
    while 1:
        strng = connection.recv(1024)
        if not strng:
            break
        if '/ENDOFFILE' in strng:
            break
        fp.write(strng)
    fp.close()
    print 'finished receive file'

    """
def deleteFile(imgName):
    imgName=mobile_directory+'/'+imgName
    try:
        os.remove(imgName)
    except OSError:
        pass
        print "deletion failed"
def PCdeleteFile(imgName):
    imgName='Files/'+imgName
    try:
        os.remove(imgName)
    except OSError:
        pass
        print "deletion failed"
        """
def PCdeleteFile(filename):
    new_filename=recycle_bin_directory+filename.split('/')[-1]
    old_filename='Files/'+filename
    os.rename(old_filename,new_filename)
def deleteFile(filename):
    new_filename=recycle_bin_directory+filename.split('/')[-1]
    old_filename=mobile_directory+'/'+filename
    os.rename(old_filename,new_filename)
def database_init(target_directory,c,db,table_name):
    print "initializing"
    for  dirPath, dirNames, fileNames in os.walk(target_directory):
        for f in fileNames:
            print "inserting " ,f
            sql= 'INSERT INTO fileNames VALUES (\''+f.encode('ascii','ignore')+'\')'
            c.execute(sql)
            db.commit()
def database_update(target_directory,table_name):
    #print "all of my tables"
    #c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(c.fetchall())
    database_list=[]
    real_list=[]
    for  dirPath, dirNames, fileNames in os.walk(target_directory):
        for f in fileNames:
            real_list.append(f)
            


    sql="SELECT name FROM "+table_name
    for row in c.execute(sql):
            print row[0].encode('ascii','ignore')
            database_list.append(row[0].encode('ascii','ignore'))

    print "database_list"
    print database_list
    print "real_list"
    print real_list

    synched=True
    for element in database_list:
        if element not in real_list:
            synched=False
            print "i should delete",element," from database"
            #useClientServer(str('/d'+target_directory+'/'+element))
            # delete not implement
            c.execute("DELETE FROM fileNames WHERE name=?", (element,))
            db.commit()

    for element in real_list:
        if element not in database_list:
            synched=False
            print "i should add",element,' to database'
            #useClientServer(str('/s'+target_directory+'/'+element))
            print "inserting",element
            sql= 'INSERT INTO fileNames VALUES (\''+element+'\')'
            c.execute(sql)
            db.commit()


    #print "update completed"
    """
        else:
            database_list.remove(element)
            real_list.remove(element)
            sql="SELECT name FROM "+table_name
            for row in c.execute(sql):
                    print row[0].encode('ascii','ignore')

            """


# Define some functions
server_directory_name='Files/'

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
##################################################
# Create table
table_name='fileNames'
target_directory="Files/client_files"
sql='SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'fileNames\'';
table_exist=False
for row in c.execute(sql):
    if str(row[0])==table_name:
        table_exist=True
db.commit()

#print table_exist
sql = 'create table if not exists ' + table_name.encode('ascii','ignore') + ' (name text)'
c.execute(sql)
db.commit()


if not table_exist:
    database_init(target_directory,c,db,table_name)

print "database ready"
table_exist=True
#####################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message :' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    while 1:
        database_update(target_directory,table_name)

    	data = conn.recv(1024) # receive byte data
        decodedstr = decodeData(data)
    	reply = decodedstr #'Message received=' + decodedstr
        print reply
        if decodedstr.startswith('/r',0,2): # client send photo request to server
            picName = decodedstr[2:]
            openAndSendBackFile(picName,conn)
        if decodedstr.startswith('/s',0,2): #client wants to send photo to server
            imageName = decodedstr[2:]
            saveFile(imageName,conn)
        if decodedstr.startswith('/S',0,2): #client wants to send photo to server
            imageName = decodedstr[2:]
            PCsaveFile(imageName,conn)

        if decodedstr.startswith('/d',0,2): #client deleted a photo
            imageName = decodedstr[2:]
            deleteFile(imageName)
        if decodedstr.startswith('/D',0,2): #client deleted a photo
            imageName = decodedstr[2:]
            PCdeleteFile(imageName)
        if decodedstr.startswith('esc',0,3):
            conn.close()
            s.close()
        if not data: 
	        break
 
conn.close()
s.close()
db.close()