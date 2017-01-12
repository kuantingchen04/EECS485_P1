CREATE TABLE IF NOT EXISTS  User
(
username varchar(20) ,
firstname varchar(20) ,
lastname varchar(20),
password varchar(20),
email varchar(40),
PRIMARY KEY (username)
);

CREATE TABLE IF NOT EXISTS  Album
(
albumid int  NOT NULL AUTO_INCREMENT, # autoincreament start from 1
title varchar(50) ,
created  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
lastupdated  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
username varchar(20),
PRIMARY KEY (albumid),
FOREIGN KEY (username) REFERENCES User(username)
);

CREATE TABLE IF NOT EXISTS  Photo
(
picid varchar(40) ,
format char(3) ,
date  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (picid)
);

CREATE TABLE IF NOT EXISTS  Contain
(
sequencenum int NOT NULL , #start from 0
albumid int, 
picid varchar(40),
caption varchar(255),
PRIMARY KEY (sequencenum),
FOREIGN KEY (albumid) REFERENCES Album(albumid),
FOREIGN KEY (picid) REFERENCES Photo(picid)
);





