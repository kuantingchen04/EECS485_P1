from flask import *
from extensions import connect_to_database
albums = Blueprint('albums', __name__, template_folder='templates')
#albums_dict={'sportslover':[['sports','I love sports','1'],['football','I love fot ball','2']],'traveler':[['world','Around the world','3']],'spacejunkie':[['space','Cool space shots','4']]}
def get_album_list(username):
	db = connect_to_database()
	cur = db.cursor()
	cur.execute('select albumid, title ,username from Album WHERE username = \''+username+'\';')
	results=cur.fetchall()
	album_list=[[r['albumid'],r['title']] for r in results]
	return album_list
def access_db(query):
	db = connect_to_database()
	cur = db.cursor()
	cur.execute(query)
	results=cur.fetchall()
	return results
@albums.route('/albums/edit',methods=['GET','POST'])
def albums_edit_route():
	if request.method=='POST':
		print (request.form.get("album_name"))
	username=request.args.get("username")
	
	options = {
		"edit": True
	}
	return render_template("albums.html", **options,username=username,album_list=get_album_list(username))

@albums.route('/albums')
def albums_route():
	#username='aaa'
	username=request.args.get("username")
	options = {
		"edit": False
		
	}
	return render_template("albums.html", **options,username=username,album_list=get_album_list(username))