from flask import *

albums = Blueprint('albums', __name__, template_folder='templates')
albums_dict={'sportslover':[['sports','I love sports','1'],['football','I love fot ball','2']],'traveler':[['world','Around the world','3']],'spacejunkie':[['space','Cool space shots','4']]}

@albums.route('/albums/edit')
def albums_edit_route():
	username=request.args.get("username")
	options = {
		"edit": True
	}
	return render_template("albums.html", **options,username=username,album_list=albums_dict[username])

@albums.route('/albums')
def albums_route():
	#username='aaa'
	username=request.args.get("username")
	options = {
		"edit": False
		
	}
	return render_template("albums.html", **options,username=username,album_list=albums_dict[username])