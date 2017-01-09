from flask import *

albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit')
def albums_edit_route():
	options = {
		"edit": True
	}
	return render_template("albums.html", **options)


@albums.route('/albums?username=<username>')
def albums_route(username):
	options = {
		"edit": False
	}
	return render_template("albums.html", **options,username=username)