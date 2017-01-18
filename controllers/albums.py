from flask import *
from extensions import connect_to_database
albums = Blueprint('albums', __name__, template_folder='templates')
#albums_dict={'sportslover':[['sports','I love sports','1'],['football','I love fot ball','2']],'traveler':[['world','Around the world','3']],'spacejunkie':[['space','Cool space shots','4']]}
def get_album_list(username):
	results=access_db('select albumid, title ,username from Album WHERE username = \''+username+'\';')
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
		if request.form.get("op") not in ["add","delete"]:
			print (request.form.get("op"))
			abort(404) 
		if request.form.get("op")=="add":
			print (request.form.get("username"))
			if not request.form.get("username"):
                        	abort(404)
			
			results_u=access_db("SELECT username FROM User WHERE username = \""+request.form.get("username")+"\"")
			
			if not results_u:
				print(request.form.get("username"))
				abort(404)
			if request.form.get("title")=="":
				abort(404)

				#page_not_found('Enter Invalid Album Name',username=request.form.get("username"))
				#return render_template("404.html",arg=request.form.get("username"),reason='Enter Invalid Album Name'), 404

			
			else: 
				print ("Input Title"+request.form.get("title"))
				max_albumid=(access_db("SELECT MAX(albumid) FROM Album")[0]['MAX(albumid)'])
				try:
					access_db("INSERT INTO Album (albumid, title, created, lastupdated, username) VALUES ("+str(max_albumid+1)+",\""+request.form.get("title")+"\",TIMESTAMP '2017-01-11 03:56:35',TIMESTAMP '2017-01-11 03:56:35',\'"+request.form.get("username")+"\');")
				except:
					print ("WJ Error!! BAD")	
					abort(404)
				return redirect(url_for('albums.albums_edit_route',username=request.form.get("username")))
			"""
                        if request.form.get("title")=="":
			    #page_not_found('Enter Invalid Album Name',username=request.form.get("username"))
			    #return render_template("404.html",arg=request.form.get("username"),reason='Enter Invalid Album Name'), 404
                            abort(404)
                        else:
                            max_albumid=(access_db("SELECT MAX(albumid) FROM Album")[0]['MAX(albumid)'])
			    access_db("INSERT INTO Album (albumid, title, created, lastupdated, username) VALUES ("+str(max_albumid+1)+",\""+request.form.get("title")+"\",TIMESTAMP '2017-01-11 03:56:35',TIMESTAMP '2017-01-11 03:56:35',\'"+request.form.get("username")+"\');")
			    return redirect(url_for('albums.albums_edit_route',username=request.form.get("username")))
			"""
		elif request.form.get("op")=="delete":
			
			
			print (request.form.get("albumid"))
			
			results=access_db("SELECT albumid , username FROM Album WHERE albumid = \""+request.form.get("albumid")+"\"")
			if not  results:
				abort(404)
			#1. select picid from Contain albumid=
			#2. delete from Contain 
			#3. delete from Photo
			#4. delete from Album
			username=results[0]["username"]
			result_d_pic=access_db("SELECT picid FROM Contain WHERE albumid=\""+request.form.get("albumid")+"\"")
			access_db("DELETE FROM Contain WHERE albumid=\""+request.form.get("albumid")+"\"")
			for pic in result_d_pic:
				access_db("DELETE FROM Photo WHERE picid=\""+pic["picid"]+"\"")
			access_db("DELETE FROM Album WHERE albumid = \""+request.form.get("albumid")+"\"")
			
			return redirect(url_for ('albums.albums_edit_route',username=username))
	if "username" not in request.args:
		abort(404)	
	username=request.args.get("username")
	results_u=access_db("SELECT username FROM User WHERE username = \""+username+"\"")
	if not results_u:
		print("Bad user: "+username)
		abort(404)

	
	options = {
		"edit": True
	}
	return render_template("albums.html", edit=True,username=username,album_list=get_album_list(username))

@albums.route('/albums')
def albums_route():
	
	if "username" not in request.args:
		abort(404)
	#username='aaa'
	username=request.args.get("username")
	#if not request.form.get("albumid"):
	#	abort(404)
	options = {
		"edit": False
		
	}
	return render_template("albums.html", edit=False,username=username,album_list=get_album_list(username))
