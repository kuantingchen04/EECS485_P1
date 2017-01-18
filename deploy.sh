# FILE: deploy.sh
 
# SERVER SPECIFIC VARIABLES
SERVER=0.0.0.0                                            # TODO set your server here!
PORT1=3000                                                                                    # TODO set your ports here!
 
# GROUP VARIABLES
GROUP=group32                                                                                # TODO set you group number
SECRET=2j0u0dsj                                                                         # TODO set your secret
GROUPDB=group32db
 
# STATIC RESOURCE paths                                                                 # TODO make sure you have a backup folder
IMAGES=static/images                                                                    # and that the paths are correct
IMAGES_BACKUP=static/images_backup
 
# SQL SCRIPT PATH                                                                               # TODO make sure paths are correct
SQL_CREATE=sql/tbl_create.sql
SQL_LOAD=sql/load_data.sql
 
# ASSIGNMENT VARIABLES
PROJECT=p1                                                                                              # TODO project number here (for sql)
 
# SCRIPT COMMANDS
echo "Resetting static resources from backup..."
rm $IMAGES/*
cp $IMAGES_BACKUP/* $IMAGES/
echo "Done."
 
echo "Resetting SQL database..."
SQL_QUERY="drop database $GROUPDB; create database $GROUPDB; use $GROUPDB; source $SQL_CREATE;"
mysql -u $GROUP -p -e "$SQL_QUERY"
echo "Done."
source venv/bin/activate
echo "starting app.py"
python app.py
echo "Done."
