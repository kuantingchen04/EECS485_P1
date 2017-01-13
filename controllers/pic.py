from flask import *
import os
import hashlib
from extensions import connect_to_database
pic = Blueprint('pic', __name__, template_folder='templates')

image_names = [ filename for filename in os.listdir('static/images')]

@pic.route('/pic')
def pic_route():
	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT * FROM Contain ;')
	results = cur.fetchall()
   
	image_list = [ result['picid'] for result in results]

	# access Album id	
	cur.execute('SELECT albumid FROM Album ;')
	results_db = cur.fetchall()
	alblum_list=[]*len(results_db)
	albid=[ int(x["albumid"]) for x in results_db]
	alblum_list=['0']*(max(albid)+1)
	for albumid in albid:
		alblum_list[albumid]=[ x['picid'] for x in results if x['albumid']==albumid]

	#image_list = [ filename for filename in os.listdir('static/image_hash')]

	pic_name=request.args.get("picid")
	#pic_name='001025dd643b0eb0661e359de86e3ea9' 
	#albumid=request.args.get("albumid")
	#albumid=1
	album_num=results[image_list.index(pic_name)]['albumid']
	#print (album_num)
	this_al=alblum_list[album_num]
	pic_num=this_al.index(pic_name)
	#print (alblum_list)
	#pic_num=1
	return render_template("pic.html",album_num=album_num,image_list=this_al,i=pic_num,len=len(this_al))
'''
if __name__ == '__main__':
	main():
		print (cur_id)
'''